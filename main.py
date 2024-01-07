import things

def main():
    # 特定のプロジェクト名を定義
    project_title = "xxx"
    # start_date = "2023-06-01"
    stop_date = "<=2023-10-31"

    todos = things.logbook()


    # タスクの一覧を表示
    for todo in todos:
        if todo.get("project_title") == project_title:  
            print(todo.get("title") + " " + todo.get("stop_date"))
            # print(todo)

if __name__ == "__main__":
    main()