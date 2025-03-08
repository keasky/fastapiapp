from google import genai

client = genai.Client(api_key="AIzaSyDFKzDMcCxZOtbyU3cYtJbi8uH9_0hUYpQ")
response = client.models.generate_content(
    model="gemini-2.0-flash", contents="AIを使った新しいアプリの例を教えてください",
)
print(response.text)