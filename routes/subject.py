from flask import Blueprint, abort, flash, redirect, render_template, request, session, url_for
from services import subject_service as service
from utils.helper import login_required
from utils.db import execute, query
from utils.validator import one_of
bp=Blueprint('subject',__name__,url_prefix='/subjects')
@bp.route('/')
@login_required
def index(): return render_template('subjects/subjects.html', subjects=service.subjects(session['user_id']))
@bp.post('/import/tu-bca-4')
@login_required
def import_tu_bca_4():
    from services.curriculum_service import import_tu_bca_fourth
    imported = import_tu_bca_fourth(session['user_id'])
    flash(f'Imported {imported} TU BCA fourth-semester subjects with units and topics.', 'success')
    return redirect(url_for('subject.index'))
@bp.route('/create',methods=['GET','POST'])
@login_required
def create():
    if request.method=='POST':
        name=request.form.get('subject_name','').strip()
        if name: service.create(session['user_id'],name,max(0,int(request.form.get('credits') or 0)),one_of(request.form.get('priority'),{'Low','Medium','High'},'Medium')); flash('Subject added.','success'); return redirect(url_for('subject.index'))
        flash('A subject name is required.','danger')
    return render_template('subjects/create.html')
@bp.route('/<int:subject_id>')
@login_required
def details(subject_id):
    subject=service.subject(session['user_id'],subject_id)
    if not subject: abort(404)
    units=service.units(subject_id)
    for unit in units:
        unit['topics'] = query('SELECT * FROM topics WHERE unit_id=%s', (unit['id'],))
    return render_template('subjects/details.html',subject=subject,units=units)
@bp.route('/<int:subject_id>/edit',methods=['GET','POST'])
@login_required
def edit(subject_id):
    subject=service.subject(session['user_id'],subject_id)
    if not subject: abort(404)
    if request.method=='POST':
        from utils.db import execute
        execute('UPDATE subjects SET subject_name=%s,credits=%s,priority=%s WHERE id=%s AND user_id=%s',(request.form['subject_name'].strip(),int(request.form.get('credits') or 0),one_of(request.form.get('priority'),{'Low','Medium','High'},'Medium'),subject_id,session['user_id']))
        flash('Subject updated.','success'); return redirect(url_for('subject.details',subject_id=subject_id))
    return render_template('subjects/edit.html',subject=subject)
@bp.post('/<int:subject_id>/units')
@login_required
def add_unit(subject_id):
    if service.subject(session['user_id'],subject_id): service.add_unit(subject_id,request.form.get('unit_name','').strip()); flash('Unit added.','success')
    return redirect(url_for('subject.details',subject_id=subject_id))
@bp.post('/units/<int:unit_id>/topics')
@login_required
def add_topic(unit_id):
    unit = query('SELECT u.id FROM units u JOIN subjects s ON s.id=u.subject_id WHERE u.id=%s AND s.user_id=%s', (unit_id,session['user_id']),one=True)
    if unit and request.form.get('topic_name','').strip(): service.add_topic(unit_id, request.form['topic_name'].strip()); flash('Topic added.','success')
    return redirect(request.referrer or url_for('subject.index'))
@bp.post('/<int:subject_id>/delete')
@login_required
def delete_subject(subject_id):
    service.delete_subject(session['user_id'], subject_id)
    flash('Subject and its units and topics were deleted.', 'success')
    return redirect(url_for('subject.index'))
@bp.post('/units/<int:unit_id>/delete')
@login_required
def delete_unit(unit_id):
    execute('DELETE u FROM units u JOIN subjects s ON s.id=u.subject_id WHERE u.id=%s AND s.user_id=%s', (unit_id, session['user_id']))
    flash('Unit and its topics were deleted.', 'success')
    return redirect(request.referrer or url_for('subject.index'))
@bp.post('/topics/<int:topic_id>/delete')
@login_required
def delete_topic(topic_id):
    execute('DELETE t FROM topics t JOIN units u ON u.id=t.unit_id JOIN subjects s ON s.id=u.subject_id WHERE t.id=%s AND s.user_id=%s', (topic_id, session['user_id']))
    flash('Topic deleted.', 'success')
    return redirect(request.referrer or url_for('subject.index'))
