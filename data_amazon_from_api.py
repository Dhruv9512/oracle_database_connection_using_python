import requests

url = "https://api-football-v1.p.rapidapi.com/v3/timezone"

headers = {
	"X-RapidAPI-Key": "45c0254d4cmsh609c58a8585388fp1f2346jsn46605d131673",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())