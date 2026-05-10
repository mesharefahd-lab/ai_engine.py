from fastapi import FastAPI
from pydantic import BaseModel
from ai_engine import MaintenanceAI # استيراد المحرك الذكي

app = FastAPI(title="Smart Maintenance System")
ai_core = MaintenanceAI()

class TicketRequest(BaseModel):
    user_name: str
    description: str
    location: str

@app.post("/request_maintenance/")
async def create_ticket(request: TicketRequest):
    # تحليل الطلب بواسطة الذكاء الاصطناعي
    analysis = ai_core.analyze_issue(request.description)
    
    return {
        "status": "Success",
        "ticket_details": {
            "requested_by": request.user_name,
            "location": request.location,
            "ai_classification": analysis["category"],
            "priority_level": analysis["priority"]
        },
        "message": "تمت الجدولة بنجاح وإشعار الفني المختص."
    }
