class Node:
    def __init__(self, digit):
        self.digit = digit
        self.next = None


class BigInteger:
    def __init__(self, number_str="0"):
        self.head = None
        self.from_string(number_str)

    # =========================
    # Membuat dari string
    # =========================
    def from_string(self, number_str):
        self.head = None
        for digit in number_str:  # simpan terbalik (LSB di depan)
            new_node = Node(int(digit))
            new_node.next = self.head
            self.head = new_node

    # =========================
    # Konversi ke string
    # =========================
    def __str__(self):
        digits = []
        current = self.head
        while current:
            digits.append(str(current.digit))
            current = current.next
        return ''.join(reversed(digits)).lstrip("0") or "0"

    # =========================
    # Visualisasi Linked List
    # =========================
    def display_list(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.digit))
            current = current.next
        print("Linked List:", " → ".join(result), "→ NULL")

    # =========================
    # Perbandingan
    # =========================
    def compare(self, other):
        s1 = str(self)
        s2 = str(other)

        if len(s1) > len(s2):
            return 1
        elif len(s1) < len(s2):
            return -1
        else:
            for a, b in zip(s1, s2):
                if a > b:
                    return 1
                elif a < b:
                    return -1
            return 0

    # =========================
    # Penjumlahan
    # =========================
    def add(self, other):
        p1, p2 = self.head, other.head
        carry = 0
        result = BigInteger("0")
        result.head = None
        tail = None

        while p1 or p2 or carry:
            val1 = p1.digit if p1 else 0
            val2 = p2.digit if p2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            new_node = Node(digit)

            if not result.head:
                result.head = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node

            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None

        return result

    # =========================
    # Pengurangan
    # =========================
    def subtract(self, other):
        if self.compare(other) < 0:
            raise ValueError("Angka pertama harus lebih besar")

        p1, p2 = self.head, other.head
        borrow = 0
        result = BigInteger("0")
        result.head = None
        tail = None

        while p1:
            val1 = p1.digit - borrow
            val2 = p2.digit if p2 else 0

            if val1 < val2:
                val1 += 10
                borrow = 1
            else:
                borrow = 0

            digit = val1 - val2
            new_node = Node(digit)

            if not result.head:
                result.head = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node

            p1 = p1.next
            p2 = p2.next if p2 else None

        return result

    # =========================
    # Perkalian (FULL LL)
    # =========================
    def multiply(self, other):
        result = BigInteger("0")

        p2 = other.head
        zero_padding = 0

        while p2:
            temp = BigInteger("0")
            temp.head = None
            tail = None

            # Tambah nol di depan (shift)
            for _ in range(zero_padding):
                new_node = Node(0)
                if not temp.head:
                    temp.head = new_node
                    tail = new_node
                else:
                    tail.next = new_node
                    tail = new_node

            carry = 0
            p1 = self.head

            while p1 or carry:
                val1 = p1.digit if p1 else 0
                mul = val1 * p2.digit + carry
                carry = mul // 10
                digit = mul % 10

                new_node = Node(digit)

                if not temp.head:
                    temp.head = new_node
                    tail = new_node
                else:
                    tail.next = new_node
                    tail = new_node

                p1 = p1.next if p1 else None

            result = result.add(temp)
            p2 = p2.next
            zero_padding += 1

        return result

    # =========================
    # Pembagian (sederhana)
    # =========================
    def divide(self, other):
        if str(other) == "0":
            raise ValueError("Tidak bisa dibagi nol")

        count = BigInteger("0")
        temp = BigInteger(str(self))

        one = BigInteger("1")

        while temp.compare(other) >= 0:
            temp = temp.subtract(other)
            count = count.add(one)

        return count


# =========================
# 🔍 CONTOH PENGGUNAAN
# =========================

a = BigInteger("12345")
b = BigInteger("678")

print("A =", a)
a.display_list()

print("B =", b)
b.display_list()

print("\nPenjumlahan:")
print("A + B =", a.add(b))

print("\nPengurangan:")
print("A - B =", a.subtract(b))

print("\nPerkalian:")
print("A * B =", a.multiply(b))

print("\nPembagian (sederhana):")
print("A / B =", a.divide(b))