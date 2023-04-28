# Perguntas geradas utilizando ChatGPT
perguntas = [
          # Fáceis
         {'titulo': 'Qual é a capital do Brasil?',
          'nivel': 'Fácil',
          'opcoes': {'A': 'Brasília', 'B': 'São Paulo', 'C': 'Rio de Janeiro', 'D': 'Belo Horizonte'},
          'correta': 'A'},
         {'titulo': 'Qual o resultado da operação 5 + 5?',
          'nivel': 'Fácil',
          'opcoes': {'A': '10', 'B': '15', 'C': '20', 'D': '25'},
          'correta': 'A'},
         {'titulo': 'Qual o resultado da operação 57 * 5?',
          'nivel': 'Fácil',
          'opcoes': {'A': '195', 'B': '314', 'C': '285', 'D': '235'},
          'correta': 'C'},
         {'titulo': 'Quando é o feriado da Independência do Brasil?',
          'nivel': 'Fácil',
          'opcoes': {'A': '21 de Abril', 'B': '12 de Outubro', 'C': '07 de Setembro', 'D': '15 de Novembro'},
          'correta': 'C'},
         {'titulo': 'Quantos títulos mundiais o Palmeiras tem?',
          'nivel': 'Fácil',
          'opcoes': {'A': '3', 'B': '4', 'C': '1', 'D': '0'},
          'correta': 'D'},
         {'titulo': 'Qual o nome do presidente do Brasil?',
          'nivel': 'Fácil',
          'opcoes': {'A': 'Jair Bolsonaro', 'B': 'Lula', 'C': 'Dilma', 'D': 'Fernando Henrique'},
          'correta': 'B'},
         {'titulo': 'Qual é o maior oceano do mundo?',
          'nivel': 'Fácil',
          'opcoes': {'A': 'Oceano Atlântico', 'B': 'Oceano Pacífico', 'C': 'Oceano Índico', 'D': 'Oceano Ártico'},
          'correta': 'B'},
         {'titulo': 'Qual é o nome do ator que interpretou Harry Potter nos filmes?',
          'nivel': 'Fácil',
          'opcoes': {'A': 'Rupert Grint', 'B': 'Daniel Radcliffe', 'C': 'Tom Felton', 'D': 'Emma Watson'},
          'correta': 'B'},
         {'titulo': 'Qual é o animal nacional da Austrália?',
          'nivel': 'Fácil',
          'opcoes': {'A': 'Canguru', 'B': 'Koala', 'C': 'Wombat', 'D': 'Diabo-da-tasmânia'},
          'correta': 'A'},
         {'titulo': 'Qual é a capital da Argentina?',
          'nivel': 'Fácil',
          'opcoes': {'A': 'Buenos Aires', 'B': 'Rio de Janeiro', 'C': 'Montevidéu', 'D': 'Assunção'},
          'correta': 'A'},
          {'titulo': 'Quantos estados tem o Brasil?',
          'nivel': 'Fácil',
          'opcoes': {'A': '24', 'B': '25', 'C': '26', 'D': '27'},
          'correta': 'D'},
          {'titulo': 'Qual é a capital da Espanha?',
          'nivel': 'Fácil',
          'opcoes': {'A': 'Madrid', 'B': 'Barcelona', 'C': 'Sevilha', 'D': 'Valência'},
          'correta': 'A'},
          {'titulo': 'Qual é o animal símbolo do Brasil?',
          'nivel': 'Fácil',
          'opcoes': {'A': 'Tucano', 'B': 'Arara', 'C': 'Onça-pintada', 'D': 'Papagaio'},
          'correta': 'C'},
          {'titulo': 'Qual é o nome do famoso cachorro criado por Mauricio de Sousa?',
          'nivel': 'Fácil',
          'opcoes': {'A': 'Lassie', 'B': 'Scooby-Doo', 'C': 'Bidu', 'D': 'Rin Tin Tin'},
          'correta': 'C'},
          {'titulo': 'Qual é o nome da primeira letra do alfabeto grego?',
          'nivel': 'Fácil',
          'opcoes': {'A': 'Alfa', 'B': 'Beta', 'C': 'Gama', 'D': 'Delta'},
          'correta': 'A'},
          {'titulo': 'Qual é o nome da capital da França?',
          'nivel': 'Fácil',
          'opcoes': {'A': 'Berlim', 'B': 'Madri', 'C': 'Paris', 'D': 'Londres'},
          'correta': 'C'},
          {'titulo': 'Qual é o nome da moeda usada no Japão?',
          'nivel': 'Fácil',
          'opcoes': {'A': 'Iene', 'B': 'Dólar', 'C': 'Euro', 'D': 'Real'},
          'correta': 'A'},
          {'titulo': 'Qual é o nome da maior ilha do mundo?',
          'nivel': 'Fácil',
          'opcoes': {'A': 'Groenlândia', 'B': 'Austrália', 'C': 'Borneo', 'D': 'Madagascar'},
          'correta': 'A'},
          {'titulo': 'Qual é a capital do Brasil?',
          'nivel': 'Fácil',
          'opcoes': {'A': 'São Paulo', 'B': 'Rio de Janeiro', 'C': 'Brasília', 'D': 'Salvador'},
          'correta': 'C'},
          {'titulo': 'Qual é o nome do principal satélite natural da Terra?',
          'nivel': 'Fácil',
          'opcoes': {'A': 'Lua', 'B': 'Sol', 'C': 'Marte', 'D': 'Vênus'},
          'correta': 'A'},
          {'titulo': 'Quem é o criador da Microsoft?',
          'nivel': 'Fácil',
          'opcoes': {'A': 'Steve Jobs', 'B': 'Bill Gates', 'C': 'Mark Zuckerberg', 'D': 'Jeff Bezos'},
          'correta': 'B'},
          {'titulo': 'Qual é o maior país da América do Sul?',
          'nivel': 'Fácil',
          'opcoes': {'A': 'Brasil', 'B': 'Argentina', 'C': 'Colômbia', 'D': 'Peru'},
          'correta': 'A'},
          {'titulo': 'Quantos planetas existem no sistema solar?',
          'nivel': 'Fácil',
          'opcoes': {'A': '7', 'B': '9', 'C': '8', 'D': '10'},
          'correta': 'C'},


          # Médias
         {'titulo': 'Quem foi o primeiro presidente dos Estados Unidos?',
          'nivel': 'Médio',
          'opcoes': {'A': 'Thomas Jefferson', 'B': 'John F. Kennedy', 'C': 'George Washington', 'D': 'Abraham Lincoln'},
          'correta': 'C'},
         {'titulo': 'Qual o nome do maior planeta do sistema solar?',
          'nivel': 'Médio',
          'opcoes': {'A': 'Júpiter', 'B': 'Saturno', 'C': 'Urano', 'D': 'Netuno'},
          'correta': 'A'},
         {'titulo': 'Qual destas não é uma linguagem de programação?',
          'nivel': 'Médio',
          'opcoes': {'A': 'C++', 'B': 'Python', 'C': 'DogeScript', 'D': 'Shiba'},
          'correta': 'D'},
         {'titulo': 'Qual destes números é primo?',
          'nivel': 'Médio',
          'opcoes': {'A': '259', 'B': '85', 'C': '49', 'D': '19'},
          'correta': 'D'},
         {'titulo': 'Qual é o nome da maior cordilheira do mundo?',
          'nivel': 'Médio',
          'opcoes': {'A': 'Andes', 'B': 'Himalaia', 'C': 'Rockies', 'D': 'Alpes'},
          'correta': 'B'},
         {'titulo': 'Qual é o nome da maior floresta tropical do mundo?',
          'nivel': 'Médio',
          'opcoes': {'A': 'Amazônia', 'B': 'Congo', 'C': 'Bornéu', 'D': 'Papua Nova Guiné'},
          'correta': 'A'},
         {'titulo': 'Quem escreveu a obra "Dom Quixote"?',
          'nivel': 'Médio',
          'opcoes': {'A': 'Miguel de Cervantes', 'B': 'William Shakespeare', 'C': 'Friedrich Nietzsche', 'D': 'Jorge Luis Borges'},
          'correta': 'A'},
          {'titulo': 'Qual é o maior animal terrestre?',
          'nivel': 'Médio',
          'opcoes': {'A': 'Elefante africano', 'B': 'Rinoceronte', 'C': 'Hipopótamo', 'D': 'Girafa'},
          'correta': 'D'},
          {'titulo': 'Em que país está localizada a cidade de Petra?',
          'nivel': 'Médio',
          'opcoes': {'A': 'Egito', 'B': 'Jordânia', 'C': 'Líbano', 'D': 'Síria'},
          'correta': 'B'},
          {'titulo': 'Qual é o nome do maior deserto do mundo?',
          'nivel': 'Médio',
          'opcoes': {'A': 'Saara', 'B': 'Gobi', 'C': 'Atacama', 'D': 'Antártica'},
          'correta': 'A'},
          {'titulo': 'Quantos elementos químicos existem na Tabela Periódica?',
          'nivel': 'Médio',
          'opcoes': {'A': '116', 'B': '118', 'C': '120', 'D': '122'},
          'correta': 'B'},


          # Difíceis
         {'titulo': 'Qual luas Júpiter tem?',
          'nivel': 'Difícil',
          'opcoes': {'A': '79', 'B': '92', 'C': '88', 'D': '54'},
          'correta': 'B'},
          {'titulo': 'Qual é o nome do cientista que propôs a teoria da relatividade?',
          'nivel': 'Difícil',
          'opcoes': {'A': 'Isaac Newton', 'B': 'Albert Einstein', 'C': 'Stephen Hawking', 'D': 'Max Planck'},
          'correta': 'B'},
          {'titulo': 'Qual é o nome do quarto estado da matéria?',
          'nivel': 'Difícil',
          'opcoes': {'A': 'Bóson', 'B': 'Plasma', 'C': 'Laser', 'D': 'Neutrino'},
          'correta': 'B'},
          {'titulo': 'Qual é o nome do mineral mais duro encontrado na Terra?',
          'nivel': 'Difícil',
          'opcoes': {'A': 'Diamante', 'B': 'Rubí', 'C': 'Topázio', 'D': 'Cristal'},
          'correta': 'A'},
          {'titulo': 'Qual é o nome do maior vulcão em atividade no mundo?',
          'nivel': 'Difícil',
          'opcoes': {'A': 'Krakatoa', 'B': 'Monte Fuji', 'C': 'Monte Etna', 'D': 'Mauna Loa'},
          'correta': 'D'},
          {'titulo': 'Qual é o nome do maior lago do mundo?',
          'nivel': 'Difícil',
          'opcoes': {'A': 'Lago Vitória', 'B': 'Lago Superior', 'C': 'Lago Baikal', 'D': 'Lago Michigan'},
          'correta': 'C'},
        ]