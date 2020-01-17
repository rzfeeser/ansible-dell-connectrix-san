- name: A playbook to connect to DS5100B
  hosts: dell
  gather_facts: no
  #become: yes

  vars:
    ansible_connection: network_cli
    ansible_password: admin12345
    ansible_user: admin
    # ansible_become_pass: password
    # ansible_user: admin
    # ansible_password: password
    # ansible_become: yes
    ansible_become_method: enable
    ansible_become_password: admin12345

  tasks:
  - name: Collect NXOS
    nxos_facts:
      gather_subset: all
    register: dellfacts
    when: ansible_network_os == 'nxos'

  - name: Display Dell Facts
    debug:
      var: dellfacts
    when: ansible_network_os == "nxos"
