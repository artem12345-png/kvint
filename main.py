from fastapi import FastAPI, APIRouter
from fastapi.responses import Response
import uvicorn
from transitions import Machine


router = APIRouter()





ids = {}
states = ['choice_size', 'choice_pay', 'check', 'bb']


@router.get('/self_check')
def self_check():
    pass
    return {'STATUS': 'OK'}


@router.get('/send_msg/{msg}/{_id}')
def send_msg(msg: str, _id: int) -> Response:
    class Offer(object):
        pass

    state = Offer()
    size = len(ids.get(_id, '   '))
    speach = {
        'choice_size': 'Какую вы хотите пиццу? Большую или маленькую?',
        'choice_pay': 'Как вы будете оплачивать?',
        'check': f"Вы хотите {ids.get(_id, '   ')[size - 2]} пиццу, оплата - {ids.get(_id, '   ')[size - 1]}",
        'bb': 'Спасибо за заказ'
    }

    transitions = [
        {'trigger': 'большую', 'source': 'choice_size', 'dest': 'choice_pay'},
        {'trigger': 'маленькую', 'source': 'choice_size', 'dest': 'choice_pay'},
        {'trigger': 'наличкой', 'source': 'choice_pay', 'dest': 'check'},
        {'trigger': 'безнал', 'source': 'choice_pay', 'dest': 'check'},
        {'trigger': 'да', 'source': 'check', 'dest': 'bb'}
    ]

    machine = Machine(state, states=states, transitions=transitions, initial='choice_size')

    if _id in ids:
        st = ids[_id][0]
        if st.state == 'bb':
            return Response('Вы уже заказали пиццу')
        msg = msg.lower()
        print(st.state)
        st.trigger(msg)
        print(st.state)
        ids[_id][0] = st
        ids[_id].append(msg)

        size = len(ids.get(_id, '   '))
        speach = {
            'choice_size': 'Какую вы хотите пиццу? Большую или маленькую?',
            'choice_pay': 'Как вы будете оплачивать?',
            'check': f"Вы хотите {ids.get(_id, '   ')[size - 2]} пиццу, оплата - {ids.get(_id, '   ')[size - 1]}?",
            'bb': 'Спасибо за заказ'
        }

        print(ids[_id])
        return Response(speach[st.state])

    else:

        size = len(ids.get(_id, '   '))
        speach = {
            'choice_size': 'Какую вы хотите пиццу? Большую или маленькую?',
            'choice_pay': 'Как вы будете оплачивать?',
            'check': f"Вы хотите {ids.get(_id, '   ')[size - 2]} пиццу, оплата - {ids.get(_id, '   ')[size - 1]}",
            'bb': 'Спасибо за заказ'
        }

        ids[_id] = ['', '', '']
        ids[_id][0] = state
        return Response(speach['choice_size'])


def init_app():
    app = FastAPI()

    app.include_router(router)
    return app


def run():
    app = init_app()
    uvicorn.run(app, host='127.0.0.1', port=4444)


if __name__ == '__main__':
    run()
