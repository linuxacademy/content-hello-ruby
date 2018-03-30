import string
import random

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

random_string = id_generator(16)

file = open("manifest-new.yml","w")
file.write("applications:\n")
file.write("- name: new-site\n")
file.write("  memory: 256m\n")
file.write("  disk_quota: 256m\n")
file.write("  path: ./new/\n")
file.write("  routes:\n")
file.write("    - route: blue-green-" + random_string + ".cfapps.io\n")
file.close()

file = open("manifest-old.yml","w")
file.write("applications:\n")
file.write("- name: old-site\n")
file.write("  memory: 256m\n")
file.write("  disk_quota: 256m\n")
file.write("  path: ./old/\n")
file.write("  routes:\n")
file.write("    - route: blue-green-" + random_string + ".cfapps.io\n")
file.close()
