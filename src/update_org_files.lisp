#-quicklisp
(let ((quicklisp-init (merge-pathnames "quicklisp/setup.lisp"
                                       (user-homedir-pathname))))
  (when (probe-file quicklisp-init)
    (load quicklisp-init)))

(ql:quickload '(:cl-sqlite :cl-who))

(defun update-org-files ()
  (let ((conn (sqlite:connect "data/project.db")))
    (let ((tables (sqlite:execute-to-list conn "SELECT name FROM sqlite_master WHERE type='table'")))
      (loop for (table) in tables
            do (let ((data (sqlite:execute-to-list conn (format nil "SELECT * FROM ~A" table))))
                 (with-open-file (stream (format nil "org/~A.org" table)
                                         :direction :output
                                         :if-exists :supersede)
                   (format stream "#+TITLE: ~A~%~%" table)
                   (format stream "* Table Contents~%")
                   (format stream "#+BEGIN_SRC lisp :results output raw :exports results~%")
                   (format stream "(cl-who:with-html-output (*standard-output*)~%")
                   (format stream "  (:table~%")
                   (format stream "    (:tr ~{(:th \"~A\")~})~%" (car data))
                   (format stream "    ~{(:tr ~{(:td \"~A\")~})~}))~%" (cdr data))
                   (format stream ")~%#+END_SRC~%")))))
    (sqlite:disconnect conn)))

(update-org-files)
