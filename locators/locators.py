from selenium.webdriver.common.by import By


class Urls:
    # phototime.pro
    phototime_pro = 'https://phototime.pro'


class Account:
    # valid test account
    phone = '9856850193'
    password = 'X8k4Keq'  # пароль будет сбрасываться после выполнения test_restore_password
    # возможно, вам потребуется создать свою учетку и подставить данные
    first_name = 'Алексей'
    last_name = 'Пшеницын'
    email = 'luufqa@gmail.com'


class Main:
    # test_main_page.py
    politic_info = (By.XPATH, './/a[text()="Политика конфиденциальности"]')
    partnership = (By.XPATH, './/button[@class="v-btn v-btn--block v-btn--outlined theme--light v-size--default '
                             'black--text"]')
    photo_news = (By.XPATH, './/button[@class="v-btn v-btn--block v-btn--outlined theme--light v-size--default '
                            'black--text"]')
    rules_in_auth_form = (By.XPATH, './/a[text()="правилами"]')


class Auth:
    # auth_user
    login_button = (By.XPATH, './/button[@class="v-btn v-btn--block v-btn--is-elevated v-btn--has-bg theme--light '
                              'v-size--default yellow"]')
    phone_field = (By.XPATH, './/input[@type="text"]')
    password_field = (By.XPATH, './/input[@type="password"]')
    accept_login = (By.XPATH, './/button[@type="submit"]')
    logout_button = (By.XPATH, './/div[@class="mt-16 v-list-item v-list-item--link theme--light"]')

    # restore_password
    restore_button = (By.XPATH, './/a[text()=" Забыли пароль? "]')
    restore_phone_field = (By.XPATH, './/input[@type="text"]')
    restore_send_password = (By.XPATH, './/span[text()=" Отправить новый пароль "]')
    restore_password_complete = (By.XPATH, './/div[text()="Новый пароль отправлен по SMS"]')


class Reg:
    # create_user
    reg_button = (By.XPATH, './/a[text()=" Регистрация "]')
    login_button_in_reg = (By.XPATH, './/a[text()=" Войти "]')
    first_name_user = (By.XPATH, './/input[@type="text"]')
    last_name_user = (By.XPATH, './/input[@type="text"]')
    phone_number_user = (By.XPATH, './/input[@type="text"]')
    email_user = (By.XPATH, './/input[@type="text"]')
    password_user = (By.XPATH, './/input[@type="password"]')
    enable_visible_password = (By.XPATH, './/button[@aria-label="append icon"]')
    accept_reg_button = (By.XPATH, './/span[text()=" Зарегистрироваться "]')
    error_alert_reg = (By.XPATH, './/div[text()="Данный пользователь уже зарегистрирован!"]')


class Search:
    # search_photo
    search_navi_button = (By.XPATH, './/*[text()="Искать фото"]')
    accept_search = (By.XPATH, './/*[text()=" Искать "]')
    search_field = (By.XPATH, './/input[@type="text"]')
    first_location = (By.XPATH, './/div[@role="option"]')
    first_photo = (By.XPATH, './/div[@class="image gallery-item"]')
    cart_photo = (By.XPATH, './/*[@class="btn v-btn v-btn--is-elevated v-btn--fab v-btn--has-bg v-btn--round '
                            'theme--light v-size--small"]')
    cart_in_search = (By.XPATH, './/*[text()="Открыть корзину (Товаров: 1)"]')


class Cart:
    # cart_menu
    cart_navi_button = (By.XPATH, './/*[text()="Корзина"]')
    buy_button = (By.XPATH, './/*[text()=" Оплатить "]')
    cart_list = (By.XPATH, './/*[text()="- Список пуст -"]')


class Payment:
    # payment_menu
    bank_card = (By.XPATH, './/a[@aria-label="Заплатить банковской картой"]')
    logout_bank_card = (By.XPATH, './/a[@target="_self"]')
    close_payment_modal = (By.XPATH, './/i[@class="v-icon notranslate mdi mdi-close theme--light"]')


class Photo:
    # download photo
    download_button = (By.XPATH,
                       './/button[@class="btn v-btn v-btn--is-elevated v-btn--fab v-btn--has-bg v-btn--round '
                       'theme--light v-size--small"]')


class Contacts:
    # contact_profile
    contacts = (By.XPATH, './/div[text()="Контакты"]')
    contacts_keys_elements = (By.XPATH, './/div[@class="text"]')
    contacts_data = ['Название: ИП Яковлев Антон Викторович',
                     'ИНН: 580505429043',
                     'ОГРНИП: 316583500103382',
                     'Расчетный счет: 40802810829170001034',
                     'Банк: ФИЛИАЛ «НИЖЕГОРОДСКИЙ» АО «АЛЬФА-БАНК»',
                     'БИК: 042202824', 'Корр. счет: 30101810200000000824',
                     'Юридический адрес: 442893, Пензенская обл, Сердобский р-н, г Сердобск, ул Тюрина, д 3, кв 78',
                     'Фактический адрес: 442893, Пензенская обл, Сердобский р-н, г Сердобск, ул Тюрина, д 3, кв 78',
                     '+7 (963) 099-48-02',
                     'Почта: vnevremeni@internet.ru',
                     'Telegram: +7 (963) 099-48-02',
                     'WhatsApp: +7 (963) 099-48-02']


class Favorite:
    # favorite_photo
    favorite = (By.XPATH, './/div[text()="Избранное"]')
    favorite_add_photo = (By.XPATH, './/button[@type="button"][2]')
    favorite_empty = (By.XPATH, './/div[text()="- Список пуст -"]')
    favorite_notification = (By.XPATH, './/span[text()="Фотография добалена в избранное"]')


class Setting:
    # setting_profile
    setting_navi_button = (By.XPATH, './/*[text()="Настройки профиля"]')
    accept_setting = (By.XPATH, './/button[@type="submit"]')
    setting_changes_complete = (By.XPATH, './/div[text()="Настройки изменены"]')
