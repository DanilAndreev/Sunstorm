def unload_in(filename, libs_count, lib_ids_in_order, books_libs_will_send):
    with open(filename, "w") as fout:
        fout.writelines([str(libs_count) + "\n"] + [str(lib_ids_in_order[i]) + " " + str(len(books_libs_will_send[i]))
                                                    + "\n" + " ".join(str(i) for i in books_libs_will_send[i]) + "\n"
                                                    for i in range(len(lib_ids_in_order))])


if __name__ == "__main__":
    unload_in("out/test.txt", 2, [1, 0], [[5, 2, 3], [0, 1, 2, 3, 4]])
