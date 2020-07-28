class AnonymousSurvey():
    """Класс для анонимных ответов."""


    def __init___(self, question):
        """Сохраняет вопрос и готовится к сохранению ответов."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Вводит вопрос."""
        print(self.question)

    def store_response(self, new_response):
        """Сохранение одного вопроса."""
        self.responses.append(new_response)

    def show_results(self):
        """Вывод полученных ответов."""
        print("Ответы на опросы:")
        for response in self.responses:
            print('- ' + response)

