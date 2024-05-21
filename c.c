#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_MENU_ITEMS 50
#define MAX_ORDERS 100
#define MAX_ORDER_ITEMS 20

typedef struct {
    char name[30];
    float price;
} MenuItem;

typedef struct {
    MenuItem items[MAX_MENU_ITEMS];
    int itemCount;
} Menu;

typedef struct {
    MenuItem item;
    int quantity;
} OrderItem;

typedef struct {
    OrderItem items[MAX_ORDER_ITEMS];
    int itemCount;
} Order;

typedef struct {
    Menu menu;
    Order orders[MAX_ORDERS];
    int orderCount;
} RestaurantBillingSystem;

void add_menu_item(RestaurantBillingSystem* system, const char* name, float price) {
    if (system->menu.itemCount < MAX_MENU_ITEMS) {
        strcpy(system->menu.items[system->menu.itemCount].name, name);
        system->menu.items[system->menu.itemCount].price = price;
        system->menu.itemCount++;
    } else {
        printf("Menu is full, cannot add more items.\n");
    }
}

void display_menu(const RestaurantBillingSystem* system) {
    printf("Menu:\n");
    for (int i = 0; i < system->menu.itemCount; i++) {
        printf("%d. %s - %.2f TK\n", i + 1, system->menu.items[i].name, system->menu.items[i].price);
    }
}

void take_order(RestaurantBillingSystem* system) {
    display_menu(system);
    Order order;
    order.itemCount = 0;
    char choice[10];
    while (1) {
        printf("Enter item number to add to order (or 'done' to finish): ");
        scanf("%s", choice);
        if (strcmp(choice, "done") == 0) {
            break;
        }
        int itemIndex = atoi(choice) - 1;
        if (itemIndex >= 0 && itemIndex < system->menu.itemCount) {
            if (order.itemCount < MAX_ORDER_ITEMS) {
                printf("Enter quantity: ");
                int quantity;
                scanf("%d", &quantity);
                order.items[order.itemCount].item = system->menu.items[itemIndex];
                order.items[order.itemCount].quantity = quantity;
                order.itemCount++;
                printf("Added %s (x%d)\n", system->menu.items[itemIndex].name, quantity);
            } else {
                printf("Order is full, cannot add more items.\n");
            }
        } else {
            printf("Invalid choice, please try again.\n");
        }
    }
    if (system->orderCount < MAX_ORDERS) {
        system->orders[system->orderCount] = order;
        system->orderCount++;
    } else {
        printf("Order list is full, cannot take more orders.\n");
    }
}

void calculate_total(const Order* order, float* total, float* tax, float* grand_total) {
    *total = 0;
    for (int i = 0; i < order->itemCount; i++) {
        *total += order->items[i].item.price * order->items[i].quantity;
    }
    *tax = *total * 0.1f;
    *grand_total = *total + *tax;
}

void generate_bill(const Order* order) {
    printf("\nBill:\n");
    for (int i = 0; i < order->itemCount; i++) {
        printf("%s (x%d) - %.2f TK\n", order->items[i].item.name, order->items[i].quantity, order->items[i].item.price * order->items[i].quantity);
    }
    float total, tax, grand_total;
    calculate_total(order, &total, &tax, &grand_total);
    printf("\nTotal: %.2f TK\n", total);
    printf("Tax (10%%): %.2f TK\n", tax);
    printf("Grand Total: %.2f TK\n\n", grand_total);
}

void run(RestaurantBillingSystem* system) {
    printf("Welcome to the Restaurant Billing System\n");
    while (1) {
        take_order(system);
        generate_bill(&system->orders[system->orderCount - 1]);
        char another_order[10];
        printf("Would you like to process another order? (yes/no): ");
        scanf("%s", another_order);
        if (strcmp(another_order, "yes") != 0) {
            break;
        }
    }
    printf("Thank you for using the Restaurant Billing System!\n");
}

int main() {
    RestaurantBillingSystem system;
    system.menu.itemCount = 0;
    system.orderCount = 0;

    add_menu_item(&system, "Pasta", 8.99f);
    add_menu_item(&system, "Pizza", 12.50f);
    add_menu_item(&system, "Salad", 5.75f);

    run(&system);

    return 0;
}
