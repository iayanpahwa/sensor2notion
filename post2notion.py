import requests, json

def createPage(databaseId, headers, data):
    createUrl = 'https://api.notion.com/v1/pages'

    newPageData = {
        "parent": { "database_id": databaseId },
        "properties": {
            "Date": {
                "title": [
                    {
                        "text": {
                            "content": data["date"]
                        }
                    }
                ]
            },
            "Outside Temperature": {
                "number": data["outsideTemperature"]
            },
            "Air Quality": {
                "rich_text": [
                    {
                        "text": {
                            "content": data["outsideAQI"]
                        }
                    }
                ]
            },
            "Home Temperature": {
                "number": data["homeTemperature"]
            },
            "Home Humidity": {
                "number": data["homeHumidity"]
            },
        }
    }

    data = json.dumps(newPageData)
    try:
        res = requests.request("POST", createUrl, headers=headers, data=data)
    except requests.exceptions.RequestException as e:
        print("Failed to post to Notion DB, check connection or API Key !!")
        raise SystemExit(e)
    else:
        #print(res)
        return(res.status_code)  
