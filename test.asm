segment .text
global _start
_start:
     ;; -- mov 34 --
     push 34
     ;; -- mov 35 --
     push 35
     ;; -- add --
     pop rax
     pop rbx
     add rax, rbx
     push rax
     ;; -- mov 500 --
     push 500
     ;; -- mov 80 --
     push 80
     ;; -- sub --
     pop rax
     pop rbx
     sub rbx, rax
     push rax
     ;; -- stk --
     ;; -- TODO     mov rax, 60
     mov rdi, 0
     syscall
