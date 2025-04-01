class BuscaBinariaCache:
    def __init__(self):
        self.cache = {}

    def busca_binaria_recursiva(self, arr, alvo, inicio=0, fim=None):
        if fim is None:
            fim = len(arr) - 1
        
        if alvo in self.cache:
            return self.cache[alvo]

        if inicio <= fim:
            meio = (inicio + fim) // 2

            if arr[meio] == alvo:
                self.cache[alvo] = meio  # Armazena o resultado no cache
                return meio

            elif arr[meio] > alvo:
                return self.busca_binaria_recursiva(arr, alvo, inicio, meio - 1)

            else:
                return self.busca_binaria_recursiva(arr, alvo, meio + 1, fim)
        else:

            self.cache[alvo] = -1 
            return -1


if __name__ == "__main__":

    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]


    bb_cache = BuscaBinariaCache()

    print(bb_cache.busca_binaria_recursiva(arr, 5))   
    print(bb_cache.busca_binaria_recursiva(arr, 15)) 
    print(bb_cache.busca_binaria_recursiva(arr, 22))  
    print(bb_cache.busca_binaria_recursiva(arr, 5))   
