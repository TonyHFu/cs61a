(define (length-tail lst)
    (define (length-helper lst length)
        (if (null? lst)
            length    
            (length-helper (cdr lst) (+ length 1))

        )
    )
    (length-helper lst 0)
)

(length-tail '(1 2 3))

(define (add-to var expr)
    (list 'define var (list '+ var expr))
)





