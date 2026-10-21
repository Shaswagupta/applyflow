from fastapi import FastAPI

app = FastAPI(
    title="ApplyFlow API",
    description="Backend for the ApplyFlow internship application platform.",
    version="0.1.0",
)


@app.get("/health", tags=["Health"])
def health_check() -> dict[str, str]:
    return {"status": "ok"}
