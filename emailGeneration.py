# import openai

# # your openai key 
# apiKey = 'OpenAiApiKey'

# openai.api_key = apiKey

# # function to generate email
# def generateEmail(name, businessDetails):
#     # email opening line
#     prompt = f"Dear {name}, {businessDetails}. Hope this email finds you well, "

#     response = openai.Completion.create(
#         engine="text-davinci-002",
#         prompt=prompt,
#         # length of the mail
#         max_tokens=100
#     )

#     emailText = response.text.strip()
#     return emailText
