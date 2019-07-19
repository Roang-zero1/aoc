from dataclasses import dataclass
from typing import Dict
import re

@dataclass
class Step:
    ident: str
    prequisites: list
    complete = False
    
    def is_ready(self) -> bool:
        if [preq for preq in self.prequisites if not preq.complete]:
            return False
        return True
    
step_regex = re.compile(r"")

def part1(steps: Dict[str, Step]) -> None:
    incomplete = steps.copy()
    step_string = ""
    while incomplete:
        print([step.ident for step in incomplete.values() if step.is_ready()])
        next_step = [step for step in incomplete if step.is_ready()][0]
        step_string += next_step.ident
        next_step.complete = True
        
        incomplete = [step for step in steps if not step.complete]
        print(step_string)

def part2() -> None:
    pass


def main():
    steps = {}
    with open("d7.txt", "r") as input_data:
        lines = input_data.readlines()
        for line in lines:
            prequisite_ident = line[5]
            step_ident = line[36]
            if prequisite_ident in steps:
                prequisite = steps[prequisite_ident]
            else:
                prequisite = Step(prequisite_ident, [])
                steps[prequisite_ident] = prequisite
            if step_ident in steps:
                steps[step_ident].prequisites.append(prequisite)
            else:
                steps[step_ident] = Step(step_ident, [prequisite])

    part1(steps)
    part2()

if __name__ == "__main__":
    main()
