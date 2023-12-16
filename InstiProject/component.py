class Question:
    def __init__(self, question, responses, options):
        self.question = question
        self.options = options
        self.responses = responses
    def Verify_Responses(self, response):
        return response == self.responses
    questions = [
        question('What is the instrument of bow that is more high-pitched sound?',
                 ["Violin", "Viola", "Cello", "Bass"],"Violin"),
        question('What is the part of the Violin, Viola and Cello that is likely between theirs',
                 ["Cavalete", "Espelho", "Cravelhas", "Queixeiras"], "Cavalete", "Espelho", "Queixeiras"),
        question('What is the afination of the Violin?', [
            "Sol, Ré, Lá, Mi", "Dó, Sol, Ré, Lá"
        ], "Sol, Ré, Lá, Mi"),
        question('What is the afination of the Viola?', [
            "Sol, Ré, Lá, Mi", "Dó, Sol, Ré, Lá"
        ],"Dó, Sol, Ré, Lá"),

    ]

    pontuacao = 0

    for question in questions:
        print(question.question)
        for i, options in enumerate(question.options):
            print(f"{i+1}.{options}")
            responses = input("Choice a correct response(1,2,3 or 4):")
            if question.verificar_resposta(question.options[int(responses)-1]):
                pontuacao +=1

            print(f"Your End pontuation is: {pontuacao}/{len(questions)}")