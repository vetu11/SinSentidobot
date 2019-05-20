# coding=utf-8
# Archivo: handlers
# Descripción: Aquí se declararán los handlers a las distintas llamadas de la API.
# Aguacate con aceite

import random
from lang import get_lang
from telegram import ParseMode, InlineQueryResultArticle, InputTextMessageContent


def generic_message(bot, update, text_code):
    # Responde a cualquier mensaje con un texto genérico, sin añadiduras.
    message = update.effective_message
    user = update.effective_user
    user_lang_code = user.language_code
    lang = get_lang(user_lang_code)

    message.reply_text(lang.get_text(text_code), parse_mode=ParseMode.MARKDOWN)


def start(bot, update):
    # Responde al comando "/start"

    generic_message(bot, update, "start")


def help(bot, update):
    # Responde al comando "/help"

    generic_message(bot, update, "help")


def more(bot, update):
    # Responde al comando "/more"

    generic_message(bot, update, "more")


def donate(bot, update):
    # Responde al comando "/donate"

    generic_message(bot, update, "donate")


def inline_query(bot, update):
    columna_1 = ["Queridos compañeros,",
                 "Por otra parte, y dados los condicionamientos actuales,",
                 "Asímismo,",
                 "Sin embargo, no hemos de olvidar que",
                 "De igual manera,",
                 "La práctica de la vida cotidiana prueba que",
                 "No es indispensable argumentar el peso y la significación de estos problemas, ya que",
                 "Las experiencias ricas y diversas muestran que",
                 "El afán de organización pero, sobre todo,",
                 "Los superiores principios ideológicos condicionan que",
                 "Incluso bien pudiéramos atrevernos a sugerir que",
                 "Es obvio señalar que",
                 "Pero pecaríamos de insinceros si soslayásemos que",
                 "Por último, y como definitivo elemento esclarecedor, cabe añadir que"]
    columna_2 = ["la realización de las premisas del programa",
                 "la complejidad de los estudios de los dirigentes",
                 "el aumento constante, en cantidad y en extensión, de nuestra actividad",
                 "la estructura actual de la organización",
                 "el nuevo modelo de actividad de la organización",
                 "el desarrollo continuo de distintas formas de actividad",
                 "nuetra actividad de información y propaganda",
                 "el reforzamiento y desarrollo de las estructuras",
                 "la consulta con los numerosos militantes",
                 "el inicio de la acción general de formación de las actitudes",
                 "un relanzamiento específico de todos los sectores implicados",
                 "la superación de experiencias periclitadas",
                 "una aplicación indiscriminada de los factores confluyentes",
                 "el proceso consensuado de unas y otras aplicaciones concurrentes"]
    columna_3 = ["nos obliga a un exhaustivo análisis",
                 "cumple un rol esencial en la formación",
                 "exige la precisión y la determinación",
                 "ayuda a la preparación y a la realización",
                 "garantiza la participación de un grupo importante en la formación",
                 "cumple deberes importantes en la determinación",
                 "facilita la creación",
                 "obstaculiza la apreciación de la importancia",
                 "ofrece un ensayo interesante de verificación",
                 "implica el proceso de reestructuración y modernización",
                 "habrá de significar un auténtico y eficaz punto de partida",
                 "permite en todo caso explicitar las razones fundamentales",
                 "asegura, en todo caso, un proceso muy sensible de inversión",
                 "deriva de una indirecta incidencia superadora"]
    columna_4 = ["de las condiciones financieras y administrativas existentes",
                 "de las directivas de desarrollo para el futuro",
                 "del sistema de participación general",
                 "de las actitudes de los miembros hacia sus deberes ineludibles",
                 "de las nuevas proposiciones",
                 "de las direcciones educativas en el sentido del progreso",
                 "del sistema de formación de cuadros que corresponda a las necesidades",
                 "de las condiciones de las actividades apropiadas",
                 "del modelo de desarrollo",
                 "de las formas de acción",
                 "de las básicas premisas adoptadas",
                 "de toda una casuística de amplio espectro",
                 "de los elementos generadores",
                 "de toda una serie de criterios ideológicamente sistematizados en un frente común de actuación regeneradora"]

    results = []

    for n in range(3):
        text = "%s %s %s %s" % (columna_1[random.randint(0,13)],
                              columna_2[random.randint(0,13)],
                              columna_3[random.randint(0,13)],
                              columna_4[random.randint(0,13)])
        results.append(InlineQueryResultArticle(id=n,
                                                title="Opción %s" % str(n + 1),
                                                description=text ,
                                                input_message_content=InputTextMessageContent(message_text=text,
                                                                                              parse_mode="Markdown")))

    update.inline_query.answer(results,
                               is_personal=True,
                               cache_time=0)
