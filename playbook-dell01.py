---
- name: Interop with Connectrix Brocade DS5100b
  hosts: dellsan
  gather_facts: no

  vars:
    credential:
      fos_ip_addr: "{{fos_ip_addr}}"
      fos_user_name: admin
      fos_password: password
      https: False

  tasks:

  - name: gather facts
    brocade_facts:
      credential: "{{credential}}"
      vfid: -1
      gather_subset:
        - brocade_time_clock_server
        - brocade_time_time_zone

  - name: print ansible_facts gathered
    debug:
      var: ansible_facts
