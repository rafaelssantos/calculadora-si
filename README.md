# calculadora-si
Repositório para a Calculadora do Sistema Internacional de Unidades (SI). Este projeto serve como enunciado para um exercício prático de desenvolvimento de software utilizando Git.

## Objetivos da atividade
Simular o trabalho em equipe em um projeto simples de desenvolvimento de uma calculadora do Sistema Internacional de Unidades, onde diferentes desenvolvedores colaboram em partes do sistema.

## Descrição do projeto
Desenvolver uma calculadora do Sistema Internacional de Unidades (SI) capaz de realizar conversões entre medidas de comprimento, massa, volume e velocidade. O desenvolvimento deve refletir a dinâmica de uma equipe de desenvolvedores, com um desenvolvedor atuando como líder do projeto.

## Uso colaborativo do Git
Cada módulo deve ser implementado em um _branch_ separado. Esse _branch_ deve ser testado antes de ser integrado. Ao final do desenvolvimento do módulo, o _branch_ deve ser mesclado à _branch_ principal.

## Atividades

### Desenvolvedor líder do projeto
- Fazer um _fork_ deste repositório.
- Compartilhar o repositório com os demais desenvolvedores.
- Gerenciar o projeto, distribuindo as tarefas entre os desenvolvedores.
- Realizar o merge das _branches_ dos módulos desenvolvidos.
- Modificar o módulo `main.py` de forma que a calculadora seja funcional.

### Demais desenvolvedores
- Implementar separadamente os seguintes módulos: `comprimento.py`, `massa.py`, `volume.py` e `velocidade.py`.

## Funcionalidades a Serem Implementadas

### Módulo `comprimento.py`
- Função para conversão de metros (m) para quilômetros (km).
- Função para conversão de quilômetros (km) para metros (m).

### Módulo `massa.py`
- Função para conversão de gramas (g) para quilogramas (kg).
- Função para conversão de quilogramas (kg) para gramas (g).

### Módulo `volume.py`
- Função para conversão de litros (l) para mililitros (ml).
- Função para conversão de mililitros (ml) para litros (l).

### Módulo `velocidade.py`
- Função para conversão de quilômetros por hora (km/h) para metros por segundo (m/s).
- Função para conversão de metros por segundo (m/s) para quilômetros por hora (km/h).

### Módulo `main.py`
- Implementar um menu para que o usuário selecione a conversão desejada.
- Capturar a entrada de dados do usuário.
- Chamar as funções correspondentes para realizar as conversões.

## Outros Requisitos
- Documentar todas as funções e módulos de forma clara e concisa.
