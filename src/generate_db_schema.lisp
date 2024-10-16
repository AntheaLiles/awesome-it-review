(ql:quickload '(:cl-sqlite :cl-dot))

(defun generate-db-schema ()
  (let ((conn (sqlite:connect "data/project.db")))
    (let ((tables (sqlite:execute-to-list conn "SELECT name FROM sqlite_master WHERE type='table'")))
      (cl-dot:dot-graph
        (cl-dot:generate-graph-from-edges
          (loop for (table) in tables
                append (loop for (column) in (sqlite:execute-to-list conn (format nil "PRAGMA table_info(~A)" table))
                             collect (cons table column))))
        "data/db_schema.svg"))
    (sqlite:disconnect conn)))

(generate-db-schema)
