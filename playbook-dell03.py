- name: A playbook to connect to DS5100B
  hosts: dell
  gather_facts: no
  #become: yes

  vars:
    ansible_connection: network_cli
    ansible_network_os: dellos9
    ansible_password: password
    ansible_user: admin
    # ansible_become_pass: password
    # ansible_user: admin
    # ansible_password: password
    # ansible_become: yes
    ansible_become_method: enable
    ansible_become_password: password
    cli:
      host: 10.127.31.41
      password: password
      username: admin
      

  tasks:
  - name: Collect Dell Facts
    cli_command:
      command: version
      # provider: "{{ cli }}"
    register: dellfacts

  - name: Display Dell Facts
    debug:
      var: dellfacts
