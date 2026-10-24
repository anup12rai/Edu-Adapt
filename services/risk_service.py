from services.dashboard_service import summary
def risk(user_id): 
    return summary(user_id)['risk']
