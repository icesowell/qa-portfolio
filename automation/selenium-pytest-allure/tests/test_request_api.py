"Testin API"
import json
import requests
import allure

@allure.feature('HeadHunter get company')
@allure.story('equal id')
def test_hh_company():
    "Получаем список компаний и сверяем данные"
    url = "https://api.hh.ru/employers?only_with_vacancies=true&text=Игра&area=113"

    response = requests.get(url, timeout=10)
    formatted_json = json.dumps(response.json(), indent=2, ensure_ascii=False)

    assert response.status_code == 200, f'Ожидали статус код 200, а пришел {response.status_code}'

    data = response.json()
    print(formatted_json)

    # Находим компанию по id и проверяем её имя
    target_company = next(
        (company for company in data["items"]
         if company["id"] == "2894825"),
        None
    )

    assert target_company is not None, "Компания с id 2894825 не найдена"
    assert target_company["name"] == "Честная игра", \
           f"У компании с id 2894825 имя '{target_company['name']}', а не 'Честная игра'"

@allure.feature('Auth + post.driver')
@allure.story('post lisense')
def test_protected_endpoint(auth_session):
    "Регистрируем водителя"
    url = "https://partner.agentapp.ru/v1/insured_objects/drivers"

    payload = ({
     "first_name": "Герман",
     "last_name": "Дольников",
     "patronymic": "Сергеевич",
     "birth_date": "1992-02-14",
     "driving_experience_started": "2018-06-25",
     "driver_licenses": [
       {
        "credential_type": "DRIVER_LICENSE",
         "number": "619605",
        "series": "7031",
        "issue_date": "2018-06-25"
      }
     ]
    })


    response = auth_session.post(url, json=payload)
    formatted_json = json.dumps(response.json(), indent=2, ensure_ascii=False)

    print(formatted_json)
