import google.generativeai as genai

print("--- Starting Gemini API Model List Test ---")

# --- PASTE YOUR NEWEST, SECRET API KEY HERE ---
API_KEY = "AIzaSyAReJQucVhjChnpgJxO1VykU2RsajR_btw"

if not API_KEY or API_KEY == "AIzaSyCxNYXuWsiT-3WIN4GwyuhVdBU4Qb_4j6E":
    print("FATAL ERROR: You did not paste your API key into the test_gemini.py file.")
    exit()

try:
    print("1. Configuring the API key...")
    genai.configure(api_key=API_KEY)

    print("2. Requesting the list of available models from the API...")
    
    model_list = []
    for m in genai.list_models():
        # We only care about models that support the 'generateContent' method
        if 'generateContent' in m.supported_generation_methods:
            model_list.append(m.name)

    print("\n--- SUCCESS! THE API CALL WORKED! ---")
    print("Here are the models available to your API key:")
    print(model_list)

except Exception as e:
    print("\n--- TEST FAILED ---")
    print("The exact error from the library is:")
    print(e)

print("\n--- Test Finished ---")