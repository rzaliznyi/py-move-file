import os


def move_file(command: str) -> None:
    parts = command.split()

    if parts[0] == "mv":
        cmd, source_file, destination_path = parts

    if os.path.exists(source_file):
        if os.path.isdir(destination_path):
            os.makedirs(destination_path, exist_ok=True)
            destination_file = os.path.join(destination_path,
                                            os.path.basename(source_file))

        else:
            if os.path.isdir(destination_path):
                destination_file = os.path.join(destination_path,
                                                os.path.basename(source_file))
            else:
                destination_file = destination_path

                os.replace(source_file, destination_file)
