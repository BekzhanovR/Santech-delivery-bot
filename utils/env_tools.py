def append_admin_id_to_env(new_id: int) -> bool:
    try:
        with open(".env", "r", encoding="utf-8") as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if line.startswith("ADMINS="):
                current_ids = line.strip().split("=")[1]
                ids_list = [i.strip() for i in current_ids.split(",") if i.strip()]
                if str(new_id) in ids_list:
                    return False  # already exists
                ids_list.append(str(new_id))
                lines[i] = f"ADMINS={','.join(ids_list)}\n"
                break

        with open(".env", "w", encoding="utf-8") as file:
            file.writelines(lines)

        return True
    except:
        return False
    
def get_admin_ids() -> list:
    try:
        with open(".env", "r", encoding="utf-8") as f:
            lines = f.readlines()
        for line in lines:
            if line.startswith("ADMINS="):
                ids = line.strip().split("=")[1]
                return list(map(int, ids.split(",")))
        return []
    except:
        return []