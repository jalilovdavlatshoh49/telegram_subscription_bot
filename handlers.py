from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from config import PAYMENT_LINK, CHANNEL_LINK
from database import add_user
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

router = Router()

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📄 Описание канала")],
        [KeyboardButton(text="💳 Оплатить подписку")],
    ],
    resize_keyboard=True
)

class PaymentState(StatesGroup):
    waiting_payment = State()

@router.message(F.text == "/start")
async def start(msg: Message, state: FSMContext):
    await msg.answer(
        "Добро пожаловать! Здесь вы можете оплатить подписку и получить доступ к закрытому каналу.",
        reply_markup=main_menu
    )

@router.message(F.text == "📄 Описание канала")
async def channel_info(msg: Message):
    await msg.answer("Этот канал предоставляет эксклюзивный контент, информацию и материалы по теме XYZ.")

@router.message(F.text == "💳 Оплатить подписку")
async def pay_subscription(msg: Message, state: FSMContext):
    await msg.answer(
        f"Чтобы оплатить подписку, переведите указанную сумму по ссылке:\n{PAYMENT_LINK}\n\n"
        "После оплаты нажмите /confirm"
    )
    await state.set_state(PaymentState.waiting_payment)

@router.message(F.text == "/confirm")
async def confirm_payment(msg: Message, state: FSMContext):
    # 🔔 Тут можно подключить реальную проверку платежей
    payment_verified = True  # <-- заменить логикой настоящей проверки

    if payment_verified:
        add_user(msg.from_user.id)
        await msg.answer(f"Оплата подтверждена! Вот ссылка на канал:\n{CHANNEL_LINK}")
        await state.clear()
    else:
        await msg.answer("Платёж не найден. Убедитесь, что вы оплатили точную сумму.")