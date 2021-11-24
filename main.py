from fastapi import FastAPI
import uvicorn
from transitions import Machine

app = FastAPI()

ids = {}
info = {
    'size': '',
    'pay_method': ''
}
states = ['choice_size', 'choice_pay', 'check', 'bb']


@app.get('/send_msg/{msg}/{id}')
def send_msg(msg: str, _id: int) -> str:

    class Offer(object):
        pass

    state = Offer()
    speach = {
        'choice_size': 'Какую вы хотите пиццу? Большую или маленькую?',
        'choice_pay': 'Как вы будете оплачивать?',
        'check': f"Вы хотите {ids[_id][1]['size']}, оплата - {ids[_id][1]['pay_method']}",
        'bb': 'Спасибо за заказ'
    }

    transitions = [
        {'trigger': 'большая', 'source': 'choice_size', 'dest': 'choice_pay'},
        {'trigger': 'маленькая', 'source': 'choice_size', 'dest': 'choice_pay'},
        {'trigger': 'наличкой', 'source': 'choice_pay', 'dest': 'check'},
        {'trigger': 'безнал', 'source': 'choice_pay', 'dest': 'check'},
        {'trigger': 'да', 'source': 'check', 'dest': 'bb'}
    ]

    machine = Machine(state, states=states, transitions=transitions, initial='')

    if id in ids:
        st = ids[id][0]
        state.trigger(st)




    return str