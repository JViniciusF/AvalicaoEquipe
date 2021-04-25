-- TABELA TypeSkill
INSERT INTO question_typeskill (type_skill) VALUES ('Entrega de Resultados');
INSERT INTO question_typeskill (type_skill) VALUES ('Autonomia');
INSERT INTO question_typeskill (type_skill) VALUES ('Proatividade');
INSERT INTO question_typeskill (type_skill) VALUES ('Colaboração');

-- TABELA Question
-- Perguntas Entrega de resultado
INSERT INTO question_question (question, type_id_id)
VALUES ('Conseguiu realizar as tasks da melhor maneira visando a entrega da atividade ?', 1);
INSERT INTO question_question (question, type_id_id)
VALUES ('Buscou garantir uma boa qualidade de entregas sem erros e bem documentadas ?', 1);
INSERT INTO question_question (question, type_id_id)
VALUES ('Na ultima sprint, manteve uma boa frequência nas entregas de suas atividades ?', 1);

-- Perguntas Autonomia
INSERT INTO question_question (question, type_id_id)
VALUES ('Conseguiu realizar as atividades propostas sem ajuda de outros membros da equipe ?', 2);
INSERT INTO question_question (question, type_id_id)
VALUES ('Preparou-se rapidamente para se adequar as suas atividades da sprint ?', 2);
INSERT INTO question_question (question, type_id_id)
VALUES ('Se você encontra um problema no projeto, você o corrige imediatamente e manteve os membros informados ?', 2);

-- Perguntas Proatividade
INSERT INTO question_question (question, type_id_id)
VALUES ('Com base nas atividades da sprint, tomou iniciativa para realizar alguma atividade sem esperar por seus companheiros de equipe ?', 3);
INSERT INTO question_question (question, type_id_id)
VALUES ('Após realizar suas atividades, buscou novas atividades para realizar antes do final da sprint ?', 3);
INSERT INTO question_question (question, type_id_id)
VALUES ('Realizou tarefas que não faziam parte das suas funções ?', 3);

-- Perguntas Colaboração
INSERT INTO question_question (question, type_id_id)
VALUES ('Ajudou os membros da equipe sempre que surgiram duvidas ou empecilhos para o andamento do projeto ?', 4);
INSERT INTO question_question (question, type_id_id)
VALUES ('Compartilhou ou buscou experiências para contribuir com o amadurecimento do projeto e dos integrantes da equipe ?', 4);
INSERT INTO question_question (question, type_id_id)
VALUES ('Manteve a equipe informada das suas atividades na sprint ?', 4);