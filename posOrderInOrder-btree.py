'''Desenvolva os métodos que recebam como parâmetros de entrada uma sequência de
nós provenientes de um percurso e imprima a árvore.
a) Pós Ordem
b) In Ordem'''

class Arvore:
    def __init__(self, valor = None):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    #função de inserção
    def inserir(self, valor):       
        if valor <= self.valor:
            if self.esquerda is None:
                self.esquerda = Arvore(valor) #uso de recursividade para criar subarvores
            else:
                self.esquerda.inserir(valor)

        else:
            if self.direita is None:
                self.direita = Arvore(valor) #uso de recursividade para criar subarvore
            else:
                self.direita.inserir(valor)                           
                        

    #inserção in ordem
    def inserirInOrdem(self, lista):
        if  not self.valor:
            if len(lista)%2 == 0:
                self.valor = lista[int(len(lista)/2)] #escolher raiz= elemento do meio
                
            else:
                self.valor = lista[int(len(lista)/2+0.5)-1]             

        for elemento in range(lista.index(self.valor)-1,-1,-1): #inserir na esquerda
            if elemento != max(lista):
                Arvore.inserir(self,lista[elemento])

        for elemento in range(lista.index(self.valor)+1,len(lista),1): #inserir na direita
            Arvore.inserir(self,lista[elemento])        

    #inserção pós ordem
    def inserirPosOrdem(self, lista): 
        if  not self.valor: #o ultimo valor da lista será a raiz
            self.valor = lista[-1]
            lista.pop(-1) #remove da lista
        aux = lista[::-1]

        for elemento in range(len(lista)):            
            Arvore.inserir(self,aux[elemento])

    #função de print in ordem
    def printInorder(self):
            if self.valor == None:
                return 
            if self.esquerda is not None:
                self.esquerda.printInorder()         
            print(self.valor)
            if self.direita is not None:    
                self.direita.printInorder()  
                

    #função de print pós ordem
    def printPostorder(self):
        if self.valor == None:
            return
            
        if self.esquerda is not None:
            self.esquerda.printPostorder()

        if self.direita is not None:
            self.direita.printPostorder()  

        print(self.valor)

    def display(self): #função para retornar saída da arvore 
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        if self.direita is None and self.esquerda is None:
            line = '%s' % self.valor
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle


        if self.direita is None:
            lines, n, p, x = self.esquerda._display_aux()
            s = '%s' % self.valor
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2


        if self.esquerda is None:
            lines, n, p, x = self.direita._display_aux()
            s = '%s' % self.valor
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        esquerda, n, p, x = self.esquerda._display_aux()
        direita, m, q, y = self.direita._display_aux()
        s = '%s' % self.valor
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            esquerda += [n * ' '] * (q - p)
        elif q < p:
            direita += [m * ' '] * (p - q)
        zipped_lines = zip(esquerda, direita)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2     
            

#árvore de busca            
root = Arvore()
root.inserirPosOrdem([1,8,4,60,20,30,10])
print()
root.printPostorder()
root.display()


#chamando funções da árvore
print()
print()
root2 = Arvore()
root2.inserirInOrdem([8, 12, 10, 26, 48, 30, 5])
root2.printInorder()
root2.display()