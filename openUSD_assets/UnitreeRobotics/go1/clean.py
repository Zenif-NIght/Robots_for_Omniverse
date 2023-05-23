with open('/home/ctaw/.local/Robots_for_Omniverse/openUSD_assets/UnitreeRobotics/go1/go1_update_modified.usda', 'r') as f:
    lines = f.readlines()

new_lines = []
skip = False
for line in lines:
    if 'def Mesh "visuals"' in line:
        skip = True
    elif skip and line.strip() == '}':
        skip = False
    elif not skip:
        new_lines.append(line)

with open('/home/ctaw/.local/Robots_for_Omniverse/openUSD_assets/UnitreeRobotics/go1/go1_update_modified_NEW.usda', 'w') as f:
    f.writelines(new_lines)
