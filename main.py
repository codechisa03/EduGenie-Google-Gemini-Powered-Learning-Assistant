from fastapi import FastAPI, Request, Form  # type: ignore
from fastapi.responses import HTMLResponse, JSONResponse  # type: ignore
from fastapi.templating import Jinja2Templates  # type: ignore
from fastapi.staticfiles import StaticFiles  # type: ignore

from qna import ask_question
from explanation_module import explain_concept
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations

app = FastAPI(title="EduGenie API")

# Setup static and templates assets
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/qa")
async def api_qa(prompt: str = Form(...)):
    result = ask_question(prompt)
    return JSONResponse(content={"result": result})

@app.post("/explain")
async def api_explain(prompt: str = Form(...)):
    result = explain_concept(prompt)
    return JSONResponse(content={"result": result})

@app.post("/quiz")
async def api_quiz(prompt: str = Form(...)):
    result = generate_quiz(prompt)
    return JSONResponse(content={"result": result})

@app.post("/summarize")
async def api_summarize(prompt: str = Form(...)):
    result = summarize_text(prompt)
    return JSONResponse(content={"result": result})

@app.post("/learn/recommendations")
async def api_recommend(prompt: str = Form(...)):
    result = get_learning_recommendations(prompt)
    return JSONResponse(content={"result": result})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
