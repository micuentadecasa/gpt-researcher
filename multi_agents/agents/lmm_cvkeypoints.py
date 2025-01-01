from .utils.views import print_agent_output
from .utils.llms import call_model
import json




class llm_cvkeypointsAgent:
    def __init__(self, websocket=None, stream_output=None, headers=None):
        self.websocket = websocket
        self.stream_output = stream_output
        self.headers = headers or {}

    async def extract_keypoints(self, content:list):
        """
        Review a cv and extract the keypoints
        :param draft_state:
        :return:
        """
        
        prompt = [
            {
                "role": "system",
                "content": "You are an expert extracting the name of the companies from a cv. Your goal is to revise cvs and extract the name of the companies where the person worked.",
            },
            {
                "role": "user",
                "content": f"""cv content:\n{content}" .
                            """,
            },
        ]
       
        if self.websocket and self.stream_output:
            await self.stream_output("logs", "key points", f"reviewing keypoints...", self.websocket)
        else:
            print_agent_output(output="reviewing keypoints..", agent="PUBLISHER")
      

        response = await call_model(
            prompt,
            model="gpt-4o",
            response_format="json",
        )
        return response

  
