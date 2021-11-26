from fastapi import FastAPI
from fastapi.responses import Response
import uvicorn
from transitions import Machine

app = FastAPI()

ids = {}

states = ['choice_size', 'choice_pay', 'check', 'bb']


@app.get('/send_msg/{msg}/{id}')
def send_msg(msg: str, _id: int) -> Response:
    """
    .jbdzvjbdzv
    :param msg:
    :param _id:
    :return:
    """

    class Offer(object):
        pass

    state = Offer()
    size = len(ids.get(_id, '   '))
    speach = {
        'choice_size': 'Какую вы хотите пиццу? Большую или маленькую?',
        'choice_pay': 'Как вы будете оплачивать?',
        'check': f"Вы хотите {ids.get(_id, '   ')[size-2]} пиццу, оплата - {ids.get(_id, '   ')[size-1]}",
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


def run():
    uvicorn.run(app, host='127.0.0.1', port=9999)


if __name__ == '__main__':
    run()
