from crewai.flow.flow import Flow, start  # Fixed capitalization
from litellm import completion
import os

os.environ["LITELLM_LOCAL_MODEL_COST"] = "False"

# Now import litellm again to ensure config is loaded
import litellm
litellm.drop_params = True  # Disable unnecessary param validation

GEMINI_API_KEY = "AIzaSyCN7yGPKTIF0OfeTNk77-uPK9POQ5VaXHs"  # Add quotes and replace with real API key

class CityFunFact(Flow):  # Fixed class name capitalization
    @start
    def generate_random_city(self):
        try:
            # Corrected parameter name from 'message' to 'messages'
            response = completion(
                model="gemini/gemini-1.5-pro",
                api_key=GEMINI_API_KEY,
                messages=[{"content": "Return a random city name. Just the name, nothing else.", "role": "user"}]
            )
            
            # Extract the city name from response
            city = response.choices[0].message.content.strip()
            print(f"Generated city: {city}")
            return city
            
        except Exception as e:
            print(f"Error: {e}")
            return "London"  # Fallback value

def kickoff():
    obj = CityFunFact()
    obj.run()  # Changed from kickoff() to run()

if __name__ == "__main__":
    kickoff()