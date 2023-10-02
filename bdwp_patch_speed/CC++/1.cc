#include <iostream>
#include <string>
using namespace std;
void a();

int main()
{
    // a();
    return 0;
}
void a()
{
    int a, b, sum;
    string out;
    cout << "x y:";
    cin >> a >> b;
    sum = a + b;
    out = to_string(a) + "+" + to_string(b) + "=" + to_string(sum);
    cout << out << endl;
}

// #include <iostream>
// #include <winsock2.h>
// #include <Windows.h>

// #include <iphlpapi.h>

// #pragma comment(lib, "iphlpapi.lib")

// int main()
// {
//     PMIB_TCPTABLE_OWNER_PID pTcpTable;
//     DWORD dwSize;

//     if (GetExtendedTcpTable(NULL, &dwSize, TRUE, AF_INET, TCP_TABLE_OWNER_PID_ALL, 0) == ERROR_INSUFFICIENT_BUFFER)
//     {
//         pTcpTable = (PMIB_TCPTABLE_OWNER_PID)malloc(dwSize);
//         if (pTcpTable != NULL)
//         {
//             if (GetExtendedTcpTable(pTcpTable, &dwSize, TRUE, AF_INET, TCP_TABLE_OWNER_PID_ALL, 0) == NO_ERROR)
//             {
//                 // Process the table, e.g., print information
//                 for (DWORD i = 0; i < pTcpTable->dwNumEntries; i++)
//                 {
//                     std::cout << "PID: " << pTcpTable->table[i].dwOwningPid << std::endl;
//                     // Add more processing as needed
//                 }
//             }
//             free(pTcpTable);
//         }
//     }

//     return 0;
// }

// #include <windows.h>
// #include <iphlpapi.h>
// #include <iostream>

// #pragma comment(lib, "iphlpapi.lib")

// int main()
// {
//     DWORD pid = 18008; // 替换为你要查询的进程的PID

//     // 获取TCP连接信息
//     MIB_TCPTABLE_OWNER_PID *tcpTable;
//     DWORD tcpTableSize = 0;

//     DWORD GetExtendedTcpTable(PVOID pTcpTable, PDWORD pdwSize, WINBOOL bOrder, ULONG ulAf, TCP_TABLE_CLASS TableClass, ULONG Reserved);

//     if (GetExtendedTcpTable(nullptr, &tcpTableSize, false, AF_INET, TCP_TABLE_OWNER_PID_ALL, 0) != ERROR_INSUFFICIENT_BUFFER)
//     {
//         std::cerr << "Error getting TCP table size." << std::endl;
//         return 1;
//     }

//     tcpTable = (MIB_TCPTABLE_OWNER_PID *)malloc(tcpTableSize);
//     if (!tcpTable)
//     {
//         std::cerr << "Memory allocation error." << std::endl;
//         return 1;
//     }

//     if (GetExtendedTcpTable(tcpTable, &tcpTableSize, false, AF_INET, TCP_TABLE_OWNER_PID_ALL, 0) != NO_ERROR)
//     {
//         std::cerr << "Error getting TCP table." << std::endl;
//         free(tcpTable);
//         return 1;
//     }

//     // 打印与指定PID相关的TCP连接信息
//     std::cout << "TCP Connections for PID " << pid << ":" << std::endl;
//     for (DWORD i = 0; i < tcpTable->dwNumEntries; ++i)
//     {
//         if (tcpTable->table[i].dwOwningPid == pid)
//         {
//             std::cout << "Local Address: " << tcpTable->table[i].dwLocalAddr << ":" << tcpTable->table[i].dwLocalPort << std::endl;
//             std::cout << "Remote Address: " << tcpTable->table[i].dwRemoteAddr << ":" << tcpTable->table[i].dwRemotePort << std::endl;
//             std::cout << "State: " << tcpTable->table[i].dwState << std::endl;
//             std::cout << "-------------------------------------" << std::endl;
//         }
//     }

//     free(tcpTable);

//     return 0;
// }
