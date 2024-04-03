from fastapi import Request, HTTPException
import conf


class BackendAuth:
    def __call__(self, request: Request):
        if conf.ENV_DEBUG == "True":
            pass
        else:
            if 'Authorization' not in request.headers:
                raise HTTPException(status_code=401, detail={"status": "error", "error": "Missing Authorization header"})
            if 'User-Agent' not in request.headers:
                raise HTTPException(status_code=401, detail={"status": "error", "error": "Missing User-Agent header"})

            token = request.headers.get('Authorization')
            user_agent = request.headers.get('User-Agent')

            if not (token == conf.ENV_DJ_SECRET) or not (user_agent == conf.BOT_AGENT_NAME):
                raise HTTPException(status_code=401, detail={"status": "error", "error": "Unauthorized"})
            if not token == conf.ENV_DJ_SECRET:
                raise HTTPException(status_code=401, detail={"status": "error", "error": "Unauthorized"})
