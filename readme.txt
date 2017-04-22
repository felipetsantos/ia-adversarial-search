/**********************************************************************
 *  Adversarial Search readme.txt template
 **********************************************************************/


Name: Felipe Teles dos Santos
Student ID: 08103842-4


Hours to complete assignment (optional): 6


/**********************************************************************
 *  Explain briefly how you implemented the helper methods for 
 * \texttt{get_next_move()}.
 **********************************************************************/
A solução foi dividida em 6 métodos auxiliares:
- min_max -> Recebe o estado atual da partida (board). Esse método é responsável por chamar o método "max", que retorna a pontuação e o movimento. O movimento é a melhor alternativa segundo o algoritmo "Mini Max" e é retornado como resultado do get_next_move().
- max -> Recebe o estado da partida e o nível da simulação. O método incrementa o nível e executa o teste terminal. Se o teste terminal retornar um resultado diferente de "None", o método retorna uma lista com a pontuação e o movimento que gerou a pontuação. Caso contrário, para cada nova jogada possível do jogador que utiliza o algoritmo, é chamado o método "min" e o resultado que tiver maior pontuação é retornado juntamente com o movimento que gerou o resultado.
- min -> Recebe o estado da partida e o nível da simulação. O método incrementa o nível e executa o teste terminal e repete o comportamento do método "max" com a diferença que, ao invés de chamar o método "min" para cada jogada possível do jogador que utiliza o algoritmo, o método chama o método "max" para cada jogada possível do jogador opositor ao que utiliza o algoritmo e retorna a menor pontuação e o movimento que gerou a pontuação.
- terminal_test -> verifica se existe um ganhador. Se sim, retorna a pontuação, se for empate, retorna zero e se ainda não terminou, retorna None.
- successors -> recebe o estado do jogo, o símbolo do jogador e retorna os próximos estados possíveis.
- score ->  Recebe o ganhador e o nível da árvore de simulação. Se o ganhador é o jogador que está utilizando o algoritmo, retorna 10 menos o valor do nível da árvore. Se o jogador for o aposto, retorna o nível da árvore de simulação menos 10. 


/**********************************************************************
 *  Explain briefly how you represented the utility of the end game. 
 * Did you use different values for different end configurations?
 **********************************************************************/
O método que testa o final do jogo verifica se existe um ganhador. Se existir, retorna a pontuação do ganhador. Caso contrário, testa se ainda há movimentos possíveis e, se existir, retorna "None". Se não existir retorna "zero", pois houve um empate.
Se houver um ganhador e o ganhador for o que está utilizando o algoritmo, retorna 10 menos a altura da árvore. Se o ganhador for o opositor, retorna a altura da árvore menos 10.




/**********************************************************************
 *  Explain briefly how you generated the successor moves.
 **********************************************************************/
A função "successors" recebe o quadro(estado do jogo) e o símbolo do player.  
A função "find_empty_cells", que veio no pacote útil do framework do trabalho, é chamada e, para cada célula vazia, é feita uma cópia do quadro, marcada a célula vazia e utilizada a palavra reservada "yield" para retornar o quadro com o movimento possível. 
Com isso, a função "successors" se transforma em uma função geradora, que gera as possibilidades de jogadas.




/**********************************************************************
 *  How often does your player wins when it plays as X against a 
 * randomizing player, and how often does it wins when it plays as O?
 **********************************************************************/
Considerando o primeiro jogador como sendo o X e utilizando algoritmo "mini max", de 100 partidas jogadas contra o random, X ganhou as 100. Nesse cenário, no formato que o algoritmo foi desenvolvido, o pior caso para X seria empate.
Considerando o primeiro jogador como sendo X e utilizando algoritmo "random", de 100 partidas jogadas contra o mini max (O), o jogador "O" ganhou 76% das partidas e empatou 24%, não teve nenhuma perda.  


/**********************************************************************
 *  If you wanted to solve some other games using variations of minimax 
 * (such as the ones seen in class), which ones would you use, and how 
 * would you integrate them into this code? Why?
 **********************************************************************/
As variações do "mini max" poderiam ser usadas para Xadrez, Dama ou até jogos mais complexos.
Para implementar o "mini max" em um jogo de dama teria que:
1. serem atribuídos valores para os estados finais;
2. ajustar o método que retorna as jogadas possíveis; 
3. ajustar o método que faz a verificação se existe ganhador;
4. definir um limite de profundidade da árvore de simulação.




/**********************************************************************
 *  If you did the extra credit, describe your algorithm briefly and
 *  state the order of growth of the running time (in the worst case)
 *  for \texttt{get_next_move()}.
 **********************************************************************/
O algoritmo é praticamente o mesmo que o "mini max". As principais mudanças foram realizadas nos métodos "min", "max" e "min_max".
- max - passou a receber dois parâmetros adicionais, "alpha" e "beta".
- min - passou a receber dois parâmetros adicionais, "alpha" e "beta".
- min_max - chama o método "max" com" alpha" vazio e "beta" vazio.
No método "max", após a chamada do método "min", além da verificação se a pontuação retornada pelo "min" é maior que a pontuação atual, também são feitas outras duas novas verificações:
- Se "beta" for diferente de vazio e o valor retornado por "min" for maior ou igual a "beta", não tem motivos para continuar a execução e o método retorna o valor que "min" retornou. Caso contrário a execução segue.
- Se "alpha" é vazio ou se valor retornado por "min" é maior que "alpha", então "alpha" recebe o valor que "min" retornou e a execução segue.

A mudança realizada no "min" é bastante similar ao que foi feito no "max" com a diferença que o primeiro teste adicional é:
- Se alpha for diferente de vazio e o valor retornado por "max" for menor ou igual a "alpha", não tem motivos para continuar a execução e o método retorna o valor que "max" retornou. Caso contrário a execução segue.
- Se "beta" é vazio ou se valor retornado por "max" é menor que "beta", então "alpha" recebe o valor que "max" retornou e a execução segue.

Essa alteração faz com que se o valor encontrado em uma folha da árvore for menor ou igual a "alpha" ou maior ou igual ao "beta", não seja necessário avaliar os outros nodos do mesmo nível, o que poda uma boa parte da árvore de simulação de jogadas. De acordo com o livro, Russell and Norvig, Capítulo 5, seção 5.4, a complexidade desse algoritmo se os sucessores forem ordenados é de O(b^(d/2)).  
 
/**********************************************************************
 *  Known bugs / limitations.
 **********************************************************************/
Nenhum bug conhecido.


/**********************************************************************
 *  Describe whatever help (if any) that you received.
 *  Don't include readings, lectures, and precepts, but do
 *  include any help from people (including staff, classmates, and 
 *  friends) and attribute them by name.
 **********************************************************************/
None




/**********************************************************************
 *  Describe any serious problems you encountered.                    
 **********************************************************************/
O maior problema foi acertar a função "teste_terminal", pois demorei para notar que meu teste não considerava corretamente o empate.




/**********************************************************************
 *  List any other comments here. Feel free to provide any feedback   
 *  on how much you learned from doing the assignment, and whether    
 *  you enjoyed doing it.                                             
 **********************************************************************/