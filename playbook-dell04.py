- name: Dell for EMC VNX
  hosts: localhost
  gather_facts: no

## For this playbook to work, we need naviseccli installed

  tasks:
  - name: Add lun to storage group
    emc_vnx_sg_member:
      name: sg01
      sp_address: 10.127.31.21
      sp_user: admin
      sp_password: password
      lunid: 100
      state: present
