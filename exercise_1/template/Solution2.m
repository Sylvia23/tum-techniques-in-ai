function Solution2(input_file_name)

%% read from txt
%  (either use the following code, or any other read_txt method you like)
input_table = readtable(input_file_name, 'ReadVariableNames',false);
input_matrix = table2cell(input_table);


%% Enter your code here.
%  Find the solution for matrix in input_filename and print the output in 'output_for_task2.txt' file
% ...
%  Assume your output matrix is of type cell


%% convert cell to table
%  write the table to a txt file
output_table = cell2table(output_matrix);
writetable(board_table, 'output_for_task2.txt', 'Delimiter',' ', 'WriteVariableNames', false);


end
