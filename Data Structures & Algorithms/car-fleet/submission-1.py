class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed),reverse = True)
        car_fleet = 0
        fleet = 0

        for pos,speed in cars:
            time = (target-pos)/speed

            if time > car_fleet:
                fleet +=1
                car_fleet = time 

        return fleet
