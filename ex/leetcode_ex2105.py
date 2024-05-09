class Solution:
    def minimumRefill(self, plants: list[int], capacityA: int, capacityB: int) -> int:
        alice_capa = capacityA
        bob_capa = capacityB
        ans = 0
        for p in range(len(plants)):
            alice_poi = p
            bob_poi = len(plants) - p - 1
            if alice_poi == bob_poi:
                    if bob_capa > alice_capa:
                        if bob_capa < plants[bob_poi]:
                            ans += 1
                    else:
                        if alice_capa < plants[alice_poi]:
                            ans += 1
                    break
            if alice_capa >= plants[alice_poi]:
                alice_capa -= plants[alice_poi]
            else:
                ans += 1
                alice_capa = capacityA - plants[alice_poi]

            if bob_capa >= plants[bob_poi]:
                bob_capa -= plants[bob_poi]
            else:
                ans += 1
                bob_capa = capacityB - plants[bob_poi]
            if len(plants) % 2 == 0:
                if alice_poi == len(plants) // 2 - 1:
                    break
        return ans