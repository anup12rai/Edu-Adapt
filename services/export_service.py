from datetime import date, timedelta
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Spacer, Paragraph, Table, TableStyle
from reportlab.lib import colors
from utils.db import query
def projected_plan(user_id, days):
    topics = query("SELECT s.subject_name,t.topic_name,s.priority FROM topics t JOIN units u ON u.id=t.unit_id JOIN subjects s ON s.id=u.subject_id WHERE s.user_id=%s AND t.status!='Completed' ORDER BY s.priority='High' DESC,u.completion ASC", (user_id,))
    return [(date.today()+timedelta(days=i), topics[i*3:i*3+3]) for i in range(days)]
def build_plan_pdf(user_id, days):
    buffer=BytesIO(); doc=SimpleDocTemplate(buffer,pagesize=A4,rightMargin=18*mm,leftMargin=18*mm,topMargin=16*mm,bottomMargin=16*mm); styles=getSampleStyleSheet()
    story=[Paragraph('Eduapt offline study plan',styles['Title']),Paragraph('This printable checklist is a snapshot. Tick completed work in Eduapt afterward to update analytics and generate the next web plan.',styles['BodyText']),Spacer(1,8*mm)]
    for day,topics in projected_plan(user_id,days):
        story.append(Paragraph(day.isoformat(),styles['Heading2'])); data=[['Done','Today\'s to-do list','Expected time']]
        for topic in topics: data.append(['',f"{topic['subject_name']} - {topic['topic_name']}",{'High':'45 min','Medium':'35 min','Low':'25 min'}.get(topic['priority'],'35 min')])
        if not topics: data.append(['[ ]','No remaining imported topics.',''])
        table=Table(data,colWidths=[18*mm,120*mm,30*mm]); table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor("#151416")),('TEXTCOLOR',(0,0),(-1,0),colors.white),('GRID',(0,0),(-1,-1),.35,colors.HexColor('#d8dce6')),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),('LEFTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)])); story += [table,Spacer(1,7*mm)]
    doc.build(story); buffer.seek(0); return buffer
