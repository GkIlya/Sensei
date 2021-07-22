from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from config import admins, channels
from filters import Users, Admin
from keyboard.default.done import done_sending
from keyboard.inline.confirm_button import confirm, offer
from loader import dp, bot
from states.state_for_channel import Get


# Ответ на кнопку


@dp.callback_query_handler(text="offerpost")
async def offer_post(call: types.CallbackQuery):
    await call.message.answer("Отправьте фото, видео, гифку или альбом поста😁")
    await Get.EnterMedia.set()


# Получение медиа для мема


@dp.message_handler(Users(), state=Get.EnterMedia, content_types=types.ContentType.ANY)
async def get_photo_mem(message: types.Message, state: FSMContext):
    if message.content_type == types.ContentType.TEXT:
        await message.answer("Супер. Теперь отправь боту фото, видео, гифку или альбом мема😡")
        return

    if message.content_type == types.ContentType.PHOTO:
        await state.update_data(photo=message.photo[-1].file_id)
    if message.content_type == types.ContentType.VIDEO:
        await state.update_data(video=message.video.file_id)
    if message.content_type == types.ContentType.ANIMATION:
        await state.update_data(gif=message.animation.file_id)
    await message.answer('Отлично. если это все нажми кнопку "готово"', reply_markup=done_sending)


# Кнопка готово


@dp.message_handler(Users(), state=Get.EnterMedia, text="Готово✅")
async def get_photo_mem(message: types.Message, state: FSMContext):
    await message.answer("Супер. Теперь отправь текст поста🗒")
    await Get.EnterText.set()


# Уточнение


@dp.message_handler(Users(), state=Get.EnterText)
async def get_text_for_post(message: types.Message, state: FSMContext):
    await message.answer("Текст успешно добавлен✅\nТеперь подтверди публикцию, после этого"
                         " пост будет отпрвлен на модерацию")
    await state.update_data(text=message.html_text, mention=message.from_user.mention,
                            notify=message.chat.id)
    await message.answer("Вы точно хотите опубликовать пост?🤨", reply_markup=confirm)
    await Get.Confirm.set()


# Ответ на уточнение


@dp.callback_query_handler(state=Get.Confirm, text="Yes")
async def poster(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        mention = data.get("mention")
        text = data.get("text")
        if data.get("photo"):
            photo = data.get("photo")
            await bot.send_message(chat_id=admins[0], text=f"Пользователь {mention} хочет опубликовать мем:")
            await bot.send_photo(chat_id=admins[0], photo=photo, caption=text, reply_markup=offer)
        if data.get("video"):
            video = data.get("video")
            await bot.send_message(chat_id=admins[0], text=f"Пользователь {mention} хочет опубликовать мем:")
            await bot.send_video(chat_id=admins[0], video=video, caption=text, reply_markup=offer)
        if data.get("gif"):
            gif = data.get("gif")
            await bot.send_message(chat_id=admins[0], text=f"Пользователь {mention} хочет опубликовать мем:")
            await bot.send_animation(chat_id=admins[0], animation=gif, caption=text, reply_markup=offer)
    await call.answer("Мем отпрвлен на проверку администратору,"
                      "спасибо за активность🤟", show_alert=True)

    await call.message.edit_reply_markup()
    await state.finish()


@dp.callback_query_handler(state=Get.Confirm, text="No")
async def poster(call: CallbackQuery, state: FSMContext):
    await call.answer("Meм был отменён, очен жаль Сенсей расстролся😔", show_alert=True)
    await call.message.edit_reply_markup()
    await state.finish()


# Напоминание об уточнение


@dp.callback_query_handler(state=Get.Confirm)
async def poster(message: types.Message):
    await message.answer('Выберите "Да" или "Нет"')


# For Admins


@dp.callback_query_handler(Admin(), text="approve")
async def approve(call: CallbackQuery, state: FSMContext):
    message = await call.message.edit_reply_markup()
    await message.send_copy(chat_id=channels[0])
    await call.answer(text="Meм был одобрен, Сенсей спокоен😌👌", show_alert=True)
    await state.finish()


@dp.callback_query_handler(Admin(), text="disapprove")
async def disapprove(call: CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    await call.answer(text="Мем отклонен, Сенсей расстроен😒😐", show_alert=True)
    await state.finish()
