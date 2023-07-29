# ctf-bitflip
### PicoCTF - MoreCookies

**Categoria**: Exploração web <br>
**Valor**: 90 pontos. <br>
**Descrição**: I forgot Cookies can Be modified Client-side, so now I decided to encrypt them! http://mercury.picoctf.net:25992/ <br>

###  Solução:

  #### 1 - O link nos direciona para a seguinte página web:
<p>"Bem-vindo à minha página de pesquisa de cookies. Somente o administrador pode usá-la!"</p>

  #### 2 - Existe um cookie chamado *auth_name* que parece ser codificado em base64:
* <p> REx6UHdUZE9hNFJkakZodXFaN1RTSzFOTXk4Z1BOa094U01ReHRoZkd3Q1l2ZGxZeThrTjZidFVJLzhMeVliVExqaVp
      Vd0ZGckI1RXRWR0VDeUI2M1l2NHM4M056MDAzWm1sUGRLL2EzYmZncytLWm9ZN2hXQnFZaGJFOVJyaVI=</p>

 #### 3 - Vamos decodificá-lo usando o Cyberchef. O resultado também parece ser codificado em base64:
 * <p>DLzPwTdOa4RdjFhuqZ7TSK1NMy8gPNkOxSMQxthfGwCYvdlYy8kN6btUI/8LyYbTLjiZUwFFrB5EtVGECyB63Yv4s
      83Nz003ZmlPdK/a3bfgs+KZoY7hWBqYhbE9RriR</p>

 #### 4 - Vamos tentar mais uma vez! Dessa vez, temos um texto sem sentido e ilegível:
 * <p>¼ÏÁ7Nk]Xn©ÓH­M3/ <ÙÅ#ÆØ_½ÙXËÉ é»T#ÿÉÓ.8SE¬DµQ zÝø³ÍÍÏM7fiOt¯ÚÝ·à³â¡áX±=F¸
                                          <br>
   
     (Isso indica que o cookie foi criptografado, de acordo com a descrição do desafio.)</p>
 
 ### Primeira Dica:
 * <p>A primeira dica é um link que nos direciona para uma página da Wikipédia sobre um método de criptografia que se chama criptografia homomórfica. <br>
   
     (A Criptografia homomórfica permite que você execute operações em texto criptografado.)</p>
 
 #### Além disso, as letras "C.B.C" estão estranhamente maiúsculas na descrição do desafio, isso quer dizer que o encadeamento de blocos cifrados (CBC) é usado.
 
* <p>O CBC depende do bloco de texto cifrado anterior para criptografar/descriptografar o pŕoximo bloco de texto simples/cifrado, ou seja, ele é vulnerável a um ataque de inversão de bits (Bit-flipping Attack).</p>

 ### Referências:<br>
 [Block Cipher Mode of Operation](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_block_chaining_(CBC))<br>
 [Cipher Block Chaining (CBC) in Cryptography](https://www.includehelp.com/cryptography/cipher-block-chaining-cbc.aspx)<br>
 [The Bit Flipping Attack](https://crypto.stackexchange.com/questions/66085/bit-flipping-attack-on-cbc-mode/66086#66086)

