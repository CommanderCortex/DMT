segment .text
     dump(unsigned long):
         push    rbp
         mov     rbp, rsp
         sub     rsp, 64
         mov     QWORD PTR [rbp-56], rdi
         mov     QWORD PTR [rbp-8], 1
         mov     eax, 32
         sub     rax, QWORD PTR [rbp-8]
         mov     BYTE PTR [rbp-48+rax], 10
     .L2:
         mov     rcx, QWORD PTR [rbp-56]
         movabs  rdx, -3689348814741910323
         mov     rax, rcx
         mul     rdx
         shr     rdx, 3
         mov     rax, rdx
         sal     rax, 2
         add     rax, rdx
         add     rax, rax
         sub     rcx, rax
         mov     rdx, rcx
         mov     eax, edx
         lea     edx, [rax+48]
         mov     eax, 31
         sub     rax, QWORD PTR [rbp-8]
         mov     BYTE PTR [rbp-48+rax], dl
         add     QWORD PTR [rbp-8], 1
         mov     rax, QWORD PTR [rbp-56]
         movabs  rdx, -3689348814741910323
         mul     rdx
         mov     rax, rdx
         shr     rax, 3
         mov     QWORD PTR [rbp-56], rax
         cmp     QWORD PTR [rbp-56], 0
         jne     .L2
         mov     eax, 32
         sub     rax, QWORD PTR [rbp-8]
         lea     rdx, [rbp-48]
         lea     rcx, [rdx+rax]
         mov     rax, QWORD PTR [rbp-8]
         mov     rdx, rax
         mov     rsi, rcx
         mov     edi, 1
         call    write
         nop
         leave
         ret
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
     sub rax, rbx
     push rax
     ;; -- hlt --
     mov rax, 60
     mov rdi, 0
     syscall
