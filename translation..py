import json
with open('settings.json', 'r') as file:
    data = json.load(file)

language = data["Language"]


if language == 'English':
    translate1 = {'Helparser': 'Helparser',
                  'Search by word': 'Search by word',
                  'Search by information': 'Search by information',
                  'Settings': 'Settings',
                  'Language: ': 'Language: ',
                  'Country: ': 'Country: ',
                  'City:': 'City:',
                  'Submit': 'Submit',
                  'Link:': 'Link:',
                  'Word:': 'Word:',
                  'Search': 'Search',
                  'Save inf': 'Save inf',
                  'Speak': 'Speak',
                  'Search words': 'Search words',
                  'Tag:': 'Tag:',
                  'Class:': 'Class:',
                  'Your country has no news': 'Your country has no news'
                }


elif language == 'Russian':
    translate1 = {'Helparser': 'Helparser',
                  'Search by word': 'Искать по слову',
                  'Search by information': 'Искать по инф.',
                  'Settings': 'Настройки',
                  'Language: ': 'Язык: ',
                  'Country: ': 'Страна: ',
                  'City:': 'Город:',
                  'Submit': 'Сохранить',
                  'Link:': 'Ссылка:',
                  'Word:': 'Слово:',
                  'Search': 'Искать',
                  'Save inf': 'Сохранить инф.',
                  'Speak': 'Озвучить',
                  'Search words': 'Search words',
                  'Tag:': 'Тег:',
                  'Class:': 'Класс:',
                  'Your country has no news': 'В вашей стране нет новостей',
                  }

elif language == 'German':
    translate1 = {'Helparser': 'Helparser',
                  'Search by word': 'Nach Wort suchen',
                  'Search by information': 'Nach Informationen suchen',
                  'Settings': 'Einstellungen',
                  'Language: ': 'Sprache: ',
                  'Country: ': 'Land: ',
                  'City:': 'Stadt:',
                  'Submit': 'Speichern',
                  'Link:': 'Link:',
                  'Word:': 'Wort:',
                  'Search': 'Suchen',
                  'Save inf': 'Informationen speichern',
                  'Speak': 'Sprechen',
                  'Search words': 'Wörter suchen',
                  'Tag:': 'Tag:',
                  'Class:': 'Klasse:',
                  'Your country has no news': 'Ihr Land hat keine Nachrichten',
                  }



elif language == 'French':
    translate1 = {'Helparser': 'Helparser',
                  'Search by word': 'Rechercher par mot',
                  'Search by information': 'Rechercher par information',
                  'Settings': 'Paramètres',
                  'Language: ': 'Langue: ',
                  'Country: ': 'Pays: ',
                  'City:': 'Ville:',
                  'Submit': 'Envoyer',
                  'Link:': 'Lien:',
                  'Word:': 'Mot:',
                  'Search': 'Rechercher',
                  'Save inf': 'Enregistrer info',
                  'Speak': 'Parler',
                  'Search words': 'Rechercher des mots',
                  'Tag:': 'Tag:',
                  'Class:': 'Classe:',
                  'Your country has no news': "Votre pays n/'a pas de nouvelles"
                  }


elif language == "Mexican":
    translate1={
        'Helparser': 'Helparser',
        'Search by word': 'Buscar por palabra',
        'Search by information': 'Buscar por información',
        'Settings': 'Configuración',
        'Language: ': 'Idioma: ',
        'Country: ': 'País: ',
        'City:': 'Ciudad:',
        'Submit': 'Guardar',
        'Link:': 'Enlace:',
        'Word:': 'Palabra:',
        'Search': 'Buscar',
        'Save inf': 'Guardar info',
        'Speak': 'Hablar',
        'Search words': 'Buscar palabras',
        'Tag:': 'Etiqueta:',
        'Class:': 'Clase:',
        'Your country has no news': 'Tu país no tiene noticias',
    }


elif language == 'Japanese':
   translate1 = {
        'Helparser': 'Helparser',
        'Search by word': '単語で検索',
        'Search by information': '情報で検索',
        'Settings': '設定',
        'Language: ': '言語: ',
        'Country: ': '国: ',
        'City:': '都市:',
        'Submit': '保存',
        'Link:': 'リンク:',
        'Word:': '言葉:',
        'Search': '検索',
        'Save inf': '情報を保存',
        'Speak': '話す',
        'Search words': '単語を検索',
        'Tag:': 'タグ:',
        'Class:': 'クラス:',
        'Your country has no news': "あなたの国にはニュースがありません",
   }


elif language == "Chinese":
    translate1 =  {
        'Helparser': 'Helparser',
        'Search by word': '按单词搜索',
        'Search by information': '按信息搜索',
        'Settings': '设置',
        'Language: ': '语言: ',
        'Country: ': '国家: ',
        'City:': '城市:',
        'Submit': '保存',
        'Link:': '链接:',
        'Word:': '词:',
        'Search': '搜索',
        'Save inf': '保存信息',
        'Speak': '说话',
        'Search words': '搜索词语',
        'Tag:': '标签:',
        'Class:': '类:',
        'Your country has no news': '你的国家没有新闻',
    }

else:
    translate1 = {'Helparser': 'Helparser',
                  'Search by word': 'Search by word',
                  'Search by information': 'Search by information',
                  'Settings': 'Settings',
                  'Language: ': 'Language: ',
                  'Country: ': 'Country: ',
                  'City:': 'City:',
                  'Submit': 'Submit',
                  'Link:': 'Link:',
                  'Word:': 'Word:',
                  'Search': 'Search',
                  'Save inf': 'Save inf',
                  'Speak': 'Speak',
                  'Search words': 'Search words',
                  'Tag:': 'Tag:',
                  'Class:': 'Class:',
                  'Your country has no news': 'Your country has no news'
    }
