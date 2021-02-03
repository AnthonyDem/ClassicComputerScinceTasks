from enum import IntEnum
from typing import List, Tuple

Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))

Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = List[Codon]

gene_str: str = 'ACGTATTGAACTGACCCTAGCCGGTTTCATAGCCGGTTCCTAGTGAGGTTCCTAGTGA'


def string_to_gene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if i + 2 >= len(s):
            return gene
        codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i + 1]], Nucleotide[s[i + 2]])
        gene.append(codon)
    return gene


my_gene = string_to_gene(gene_str)


def linear_contains(gene: Gene, key_codon: Codon) -> bool:
    for g in gene:
        if g == key_codon:
            return True
    return False


def binary_contains(gene: Gene, key_codon: Codon) -> bool:
    low: int = 0
    high: int = len(gene) - 1
    while low <= high:
        mid: int = (low + high) // 2
        if gene[mid] < key_codon:
            low = mid + 1
        elif gene[mid] > key_codon:
            high = mid - 1
        else:
            return True
    return False


my_sorted_gene: Gene = sorted(my_gene)